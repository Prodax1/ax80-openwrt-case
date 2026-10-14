# Build configurations

`installed-era/` contains the saved custom-01 and recovery-02 full `.config` plus diffconfig, and the actual candidate-04 U-Boot config. These are from the build era of the installed custom case; they do not certify that every output was installed. Closed-component inputs, files overlays, VPN servers, runtime UCI, Wi-Fi settings and private keys are excluded. Those omissions prevent byte-identical reproduction of the old custom images from this repository alone.

`rebased/` contains the full clean-build Kconfig, diffconfig and feed revisions for both EU profiles compiled on c45a44104b. It selects per-device rootfs and an external GCC 14.3.0/musl toolchain. Absolute toolchain paths are anonymized; use an equivalent verified environment before make defconfig. Do not mistake these build configs for settings to import into a router.

Compare `.config` after dependency resolution, not only a seed. The clean U-Boot redundant-env finding is recorded separately in [evidence/rebased-uboot-env.txt](../evidence/rebased-uboot-env.txt). Config/package selection does not authorize firmware distribution.
