# Patches: what was actually used

These are source records, not a universal flashing kit. Read [the stages](../docs/README.md) first. Baseline and target contexts differ; never apply all files as one series.

| File | Actual role | Application scope |
| --- | --- | --- |
| upstream/pr21640-original.diff | Board support underpinning the October custom installation | Against the PR's original base, not a random current main |
| upstream/ax80-eu-ubi-rebased.diff | Two upstream commits compiled on the October 13 main snapshot | Against 3fba6794e2; excludes the five local patches |
| local/env-redundant-port-fix.patch | Custom U-Boot enabled current redundant-env Kconfig | U-Boot 2026.01 source after board patches |
| local/hardened-env.patch | Custom env error handling and BL2/FIP size/hash gates | Historical migration policy; not atomic or upstream-ready |
| local/ram-uboot-no-nand.patch | RAM diagnostic loader with NAND disabled | Diagnostic variant only; never a permanent NAND loader |
| local/recovery-no-bootloader.patch | Suppressed exported bootloader artifacts in recovery build | Output packaging; does not enforce NAND write protection |
| local/awg-crypto-select.patch | Extra custom module selected kernel crypto via WireGuard | Custom package, not board support; absent from clean rebase |

Upstream diff address literals are replaced with `<ADDRESS>` where present, so an archive requiring those values is not apply-and-build-ready. Sanitization does not silently supply addresses. No optional review-fixup or unexecuted installation proposal is included as used code.

See [ATTRIBUTION.md](../ATTRIBUTION.md), [LICENSE](../LICENSE), [PR #21640](https://github.com/openwrt/openwrt/pull/21640), [test comment](https://github.com/openwrt/openwrt/pull/21640#issuecomment-6175000087), and [forum 242149](https://forum.openwrt.org/t/242149).
