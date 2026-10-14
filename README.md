# How one Archer AX80 EU ended up with a new bootchain

[Русская версия](README.ru.md)

I wanted a router that could hold the software I actually used without depending on a USB stick for its writable storage. My TP-Link Archer AX80 **EU v1.0** already had OpenWrt alongside the vendor system. It worked, but the two-slot flash arrangement left much less useful space than the chip's advertised capacity suggested.

This repository tells what happened next: the failed attempts, the checks that changed the plan, the local source changes, and the eventual boot from a replacement BL2/TF-A/U-Boot chain with one UBI area. It is **one case, not an installation guide**. I did it without an attached UART adapter; that was a risk accepted for this device, not evidence that UART is unnecessary. A failed bootloader write can leave a brick with no network recovery. Losing the original Wi-Fi calibration can leave a booting router with broken radios.

## The route was not straight

1. **The big image failed.** On 7 October a roughly 50.4 MB custom image did not boot and the device returned to the vendor system. The earlier OpenWrt slot had roughly 44 MB of real capacity. Oversize was a likely explanation; the vendor boot counter was another possibility. We did not establish which one caused the failure. `sysupgrade -T` accepting the file had not checked that capacity.
2. **Backups came before another attempt.** Starting from vendor firmware 1.1.2, we obtained temporary administrative access through the telnet-enable method. We read the seven exposed partitions twice and checked the factory files separately. Those reads covered 123 MiB, not the whole 128 MiB chip or its OOB data.
3. **A diagnostic image worked, but led to a dead end.** We enlarged the old kernel volume, wrote a read-only diagnostic FIT and booted it. It exposed the missing NAND tail and allowed a full 128 MiB partition-data backup. It also refused NAND writes. There was no demonstrated kexec exit. We had to use the vendor recovery route while the vendor chain still existed, return to stock, and take a different route into a writable migration initramfs.
4. **The bootchain was prepared offline.** The custom loader enabled the current redundant-env option and added checks around TFTP and write failures. We checked FIT contents, UBI geometry, payload sizes and environment CRCs. We filled the two environment copies in advance so first boot would select recovery without depending on an interactive firstboot menu.
5. **The flash changed in three separate stages.** Factory data prepared from this router's own backup went first, then the unified UBI image, then BL2. Each stage had readback checks. This was not an atomic transaction: a power failure in the middle could still have made it unbootable.
6. **Recovery booted, then production booted.** The first boot used the RAM recovery system from its stored FIT. After a separate environment change, the production system booted from internal NAND. An ordinary reboot later retained settings. USB extroot was no longer needed.

The detailed record, including historical commands and their explanations, starts at [docs/README.md](docs/README.md). Commands that wrote flash are shown as evidence, with private paths removed. There is no ready-to-run migration installer.

## What actually worked

The installed custom system reported `tplink,archer-ax80-v1-eu-ubi`, OpenWrt SNAPSHOT `r0-d4ebffe5`, Linux `6.18.26`, SquashFS `/rom` and a writable internal UBIFS overlay. Its six volumes were `fip`, `ubootenv`, `ubootenv2`, `fit`, `recovery`, and `rootfs_data`. The later audit had about 27.9 MiB of free overlay space. Calibration readback matched the prepared private factory backup; this checks preservation, not radio performance.

Ethernet access and router-originated DNS/HTTPS worked. Both Wi-Fi APs were enabled by the audit. A physical WPS press opened PBC on both radios for 120 seconds, but no client was paired. Some LED indication and software button handlers were checked. NAND health counters showed no reported failures or bad blocks in the saved snapshot.

## Three builds, three different claims

| Set | What the record supports |
| --- | --- |
| Custom October 8–9 installation | Recovery, production and ordinary production reboot observed on one router, with local changes |
| Later custom rebuild | Offline checks only; production exceeds the old FIT volume, recovery has only 73,728 bytes of headroom; not ready to flash |
| October 13 rebase | Both EU profiles compiled; six artifacts checked; never run on the router; clean loader still lacks enabled redundant env |

The rebase preserved the two upstream commits and resolved only the board-list conflicts. Its first build hit a shell error because Windows paths containing parentheses entered WSL's `PATH`; rebuilding with a Linux-only `PATH` succeeded. None of our five old local patches was applied to that clean rebase. An optional review fixup was inspected but not built; it is not presented here as used migration code.

## What remains unknown

Physical recovery-button entry, UART restoration, returning this new layout to stock, deliberate failure recovery, WPS client pairing, every Ethernet port, Wi-Fi throughput, client VPN/DNS/IPv6 behavior and sustained load were not demonstrated. The vendor dual-slot fallback is gone. Reset selecting TFTP is an inference from the saved environment, not a tested rescue procedure. U-Boot cannot promise fallback once it has handed control to a hung kernel.

## Where the work is

- [Detailed stages and glossary](docs/README.md)
- [Patches and attribution](patches/README.md)
- [Historical scripts](scripts/README.md) and [build configs](configs/README.md)
- [Evidence and its limits](evidence/README.md)
- [Firmware inventory with recomputed SHA256](RELEASES.md); no binaries in git
- [Sanitization report](SANITIZE-REPORT.md) and [license: GPL-2.0](LICENSE)

The board support belongs to its upstream contributors. See [OpenWrt PR #21640](https://github.com/openwrt/openwrt/pull/21640), [the posted test comment](https://github.com/openwrt/openwrt/pull/21640#issuecomment-6175000087), and [forum topic 242149](https://forum.openwrt.org/t/242149). PR #19440 and the E8450/RT3200 UBI installer informed research; neither supplies interchangeable AX80 binaries.

## Publication boundaries

This draft contains no subscription URLs, account credentials, private keys, original NAND dumps, configuration archives, serial/MAC identifiers, or private network/service addresses. Custom firmware containing proprietary VPN binaries is not distributed here. Any future source patch needs its own attribution, license review, tests, and owner approval before publication.
