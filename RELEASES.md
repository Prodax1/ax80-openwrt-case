# Local firmware inventory — no release published

No firmware binary is in this repository. This table records local files whose SHA256 and size were recomputed during preparation. A matching hash checks identity, not compatibility or recovery safety.

- **installed-era**: recovery/production built during the migration; boot observations are for that custom installation, not for every file here.
- **later-unbooted**: later custom donor rebuild; never installed/boot-tested, `ready_to_flash=false`.
- **research-bootchain**: offline BL2/BL31/U-Boot/FIP candidates; the inventory alone does not identify the installed bootloader.
- **rebased-build-only**: six clean artifacts compiled on the rebased branch; none run on hardware.

The old custom recovery/production images contain a proprietary component and must not be redistributed. No such binary or license grant is provided here. The owner decides whether a future source-complete, legally distributable build deserves a GitHub Release. Device-specific factory, seeded UBI and full NAND backups are excluded even from this inventory.

| Group | Local artifact | Bytes | SHA256 |
| --- | --- | ---: | --- |
| installed-era | `completed-images-20261008T215302Z-179979/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-initramfs-recovery.itb` | 27721728 | `df4f7710cf6e7def345dfb6b00de83e6faf5883c42c8dccb370e1967e130a96f` |
| installed-era | `completed-images-20261008T215302Z-179979/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-squashfs-sysupgrade.itb` | 52789539 | `4885a5ffda4d4904fb76c7b810fce0eac8d7b8e9f466963215a119f833fffc00` |
| later-unbooted | `donor-rebuild-20261009T143346Z-338/production/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-squashfs-sysupgrade.itb` | 53121315 | `db595ed2e4df23faedacb89286e6a06f53ed020b466e3bdcfe26b79cbfa1a58f` |
| later-unbooted | `donor-rebuild-20261009T143346Z-338/recovery/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-initramfs-recovery.itb` | 30146560 | `873cb5757e1866bcff7b3fc62a3700c1a4d49c90947e330215afed585d8e9be2` |
| research-bootchain | `artifacts-research-only/bl2.img` | 156247 | `059452a3d02b9d010bc99cebf92bccce2e360ef34020650ff2308393ea19fe03` |
| research-bootchain | `artifacts-research-only/bl31.bin` | 33452 | `659364afaa54b5e6e737a2a54fd8dd808e43d5dd77ddd9c866eca915239f37cd` |
| research-bootchain | `artifacts-research-only/research-bl31-uboot.fip` | 1002804 | `871abd7fdc0f36916a1aaa6e8bf6c8e4f56efca80fc316b4bbb87c30993dc7b1` |
| research-bootchain | `artifacts-research-only/u-boot.bin` | 969216 | `26ff526bcdeb9d0c9ced30f0b9addb45572e6b011db522c3811bad9a094c377c` |
| research-bootchain | `artifacts-candidate04-research-only/bl2.img` | 156247 | `5c01eb74ef38218d69256cd3a2098bc5ca49ef5471e6aad91f4f43b25ad92cfa` |
| research-bootchain | `artifacts-candidate04-research-only/bl31.bin` | 33452 | `744f716332e0f35b10d21cb4ebbc3869b67711954e6fbda97193e1345747e20a` |
| research-bootchain | `artifacts-candidate04-research-only/research-bl31-uboot.fip` | 1004628 | `40a7887876b300d534a57ea6ae71692d02fd6e49ea6536d78807b7bffa5be5f8` |
| research-bootchain | `artifacts-candidate04-research-only/u-boot.bin` | 970960 | `f92e7a4f3311c82d7dbd16bdfbb9e6e0642be387908c0e08130199045225104a` |
| rebased-build-only | `upstream-pr/artifacts/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-initramfs-kernel.bin` | 9365288 | `3da3a6bdaeaf3069585086159f9de3e5de5e504188ee5f734acffca88aab1f92` |
| rebased-build-only | `upstream-pr/artifacts/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-squashfs-sysupgrade.bin` | 10045731 | `cc93aefaeb15e634cdd986c975f14df16bce2688c1bc566f214e979dfc33f0a5` |
| rebased-build-only | `upstream-pr/artifacts/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-bl31-uboot.fip` | 1023188 | `b04eb76ed51f2e2865974f741f29ace0a61299395dea001fb23dcaba6a93e831` |
| rebased-build-only | `upstream-pr/artifacts/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-initramfs-recovery.itb` | 9240576 | `c68abfea90693006efbb70b0d6a7e444a5ca94825b3cbf9fde5f252a01fbaaee` |
| rebased-build-only | `upstream-pr/artifacts/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-preloader.bin` | 156247 | `1d0ffa78db92a790f7c2923a5e7793537f8da4c45c0b96ff883d6d2fcba9fc06` |
| rebased-build-only | `upstream-pr/artifacts/openwrt-mediatek-filogic-tplink_archer-ax80-v1-eu-ubi-squashfs-sysupgrade.itb` | 11612459 | `6fc1984cf1be8a041d8087c59193403791005b9f45433751514bb5897cb18d6d` |
