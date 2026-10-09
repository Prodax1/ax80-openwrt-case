# Archer AX80 EU v1: replacement bootchain and unified UBI case report

Draft for owner review. Not an installer, not a release, and not a universal flashing guide.

## Scope and attribution

This report describes one owner's TP-Link Archer AX80 EU hardware revision v1.0. The device was migrated from the vendor bootchain and its two-slot arrangement to a replacement BL2/TF-A/U-Boot chain with production and recovery images in a unified UBI layout.

The migration was performed without a connected UART adapter. That is an observation about one attempt, NOT a recommendation to omit UART or a claim of safe recovery without it. A wrong bootloader, interrupted write, or incompatible NAND layout can make network recovery unavailable. Backups alone do not provide a working restoration interface.

Relevant upstream work, rather than original board support claimed by this report:

- [OpenWrt PR #19440: Archer AX80 U-Boot/UBI layout proposal](https://github.com/openwrt/openwrt/pull/19440).
- [OpenWrt PR #21640: related AX80 UBI support work](https://github.com/openwrt/openwrt/pull/21640).
- [dangowrt/owrt-ubi-installer](https://github.com/dangowrt/owrt-ubi-installer): conceptual reference for an installer carrying a replacement bootchain and recovery image. Its documented targets include Linksys E8450 and Belkin RT3200; their images are NOT AX80 images.

No upstream PR status or release-support claim is implied. Check the linked projects before selecting a build.

## Starting point and preparation

The vendor firmware used for initial access was 1.1.2. Root access was obtained through the device's telnet-enable method. The router had previously used a vendor/OpenWrt two-slot setup; the available persistent space was insufficient for the desired custom package set.

Preparation included repeated backup verification, analysis of the existing NAND/bootchain, initramfs diagnostics, Linux/WSL builds, FIT compatibility and hash checks, UBI geometry checks, environment CRC checks, and comparison of the factory/calibration partition before and after migration.

An early read-only diagnostic image did not permit migration. The vendor recovery path was used during that earlier stage. Those vendor recovery procedures must not be assumed to apply after replacing the bootchain and layout. Running from initramfs does not itself remove MTD write protection: that depends on the kernel/device tree and the actual target mapping.

This draft deliberately omits destructive commands and installation artifacts. It is not sufficient to reproduce the migration.

## Observed result

The replacement chain booted recovery and then production. A subsequent ordinary reboot successfully booted production from internal NAND, with persistent settings and the same SSH host identity.

| Item | Observed state in the local audit |
| --- | --- |
| Board identifier | `tplink,archer-ax80-v1-eu-ubi` |
| Build source | OpenWrt commit `d4ebffe538ab94d9b5a604f4bba28325f38ed3d8` |
| Running system | SNAPSHOT `r0-d4ebffe5`, Linux `6.18.26` |
| Persistent storage | SquashFS `/rom`, read/write UBIFS overlay on internal NAND |
| UBI volumes | `fip`, `ubootenv`, `ubootenv2`, `fit`, `recovery`, `rootfs_data` |
| Protected partitions | Boot/BL2/factory read-only in the running production system |
| Factory data | SHA-256 matched the retained pre-migration factory backup |
| Environment | Both copies had valid CRCs; environment tools used the actual UBI volumes |
| NAND counters | No ECC failures or bad blocks reported in the audit snapshot |
| Available overlay | Approximately 27.9 MiB free at the audit snapshot |
| Wi-Fi | Both access points enabled; client traffic not tested in this audit |
| USB | Storage/ext4 device detected; no USB extroot dependency |

These are snapshot observations, not flash endurance tests or proof that all hardware paths work.

## Follow-up findings potentially useful upstream

1. Environment utilities must describe the real redundant environment volumes and their LEB geometry, rather than reuse settings for the vendor layout.
2. A production FIT exceeding the existing `fit` volume is not automatically incompatible with standard sysupgrade. The inspected board updater used `fit_do_upgrade`, `nand_upgrade_fit`, and `nand_upgrade_prepare_ubi` to recreate the production FIT and writable data volumes. Directly writing the larger image into the old volume would not fit. This updater path was inspected, not exercised with the later rebuilt images.
3. The front WPS button opened PBC on both APs for 120 seconds using full `wpad-mbedtls` and `hostapd-utils`. An existing hostapd process had to be replaced after package changes. Client pairing remains untested.
4. AP netdev `link/tx/rx` triggers restored the expected Wi-Fi LED indication in this custom configuration. This does not establish a general defect in the upstream radio triggers.
5. A custom rear-button handler implements short press for LEDs and a hold of at least two seconds for Wi-Fi. Software LED toggling was checked; physical short/long press validation remains pending.
6. USB storage detection and the configured USB presence LED were checked. Physical removal behavior remains pending.

These are candidates for focused patches after checking the current upstream implementation. No upstream-ready code patch is included in this draft.

## Recovery and update limits

The inspected boot command checks buttons, attempts production, then recovery, then TFTP. This does NOT guarantee fallback after a kernel hangs once U-Boot has handed over execution.

The recovery image previously booted, but the physical recovery-button path and intentional failure recovery have not been tested. UART-assisted restoration has not been tested. A later rebuilt production/recovery pair passed offline validation but was NOT installed or boot-tested, and remains explicitly not ready to flash.

During the audit the existing production FIT volume was 52,822,016 bytes. The later production image was 53,121,315 bytes and would require volume recreation by the applicable updater. The later recovery image was 30,146,560 bytes against a 30,220,288-byte recovery volume, leaving only 73,728 bytes. Future growth requires renewed size and layout checks.

For normal updates, do not rerun a migration installer or replace BL2/FIP unnecessarily. Preserved configuration archives need separate review because they can restore old init scripts and overrides over a new image.

## Not yet demonstrated

- Client internet/VPN routing, DNS/IPv6 behavior, subscription device headers, or performance under load.
- WPS client pairing, physical rear-button behavior, and USB removal handling.
- Physical recovery entry, failure fallback, or restoration through UART.
- Hardware boot of the later rebuilt image pair.
- Applicability to other AX80 regions, hardware revisions, NAND geometries, or firmware versions.

## Publication boundaries

This draft contains no subscription URLs, account credentials, private keys, original NAND dumps, configuration archives, serial/MAC identifiers, or private network/service addresses. Custom firmware containing proprietary VPN binaries is not distributed here. Any future source patch needs its own attribution, license review, tests, and owner approval before publication.
