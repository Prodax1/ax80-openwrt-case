# Sources and confidence

The repository was assembled from local source records; no SSH or device operation was performed while preparing it. The context directory was read only. Its earlier planning notes were treated as history where superseded by completed checkpoints.

| Claim | Local source record |
| --- | --- |
| Failed large image and slot-capacity hypothesis | Firmware-build memory note, October 7 incident; not a proven root cause |
| Two stock backup sets, 20 checks, missing tail/OOB | AX80-BACKUP-VERIFICATION-2026-10-08.md |
| Diagnostic resize, write, boot; later additions supersede proposal | AX80-STOCK-FIT-DELIVERY-2026-10-09.md |
| Read-only exit dead end and vendor recovery route | AX80-MIGRATION-TRANSITION-2026-10-09.md; reference-to-migration result |
| Offline factory/UBI/env/DDR preparation | AX80-FIRSTBOOT-DDR-RESULT-2026-10-09.md; prepare_* sources |
| Three writes, no reboot yet | AX80-FLASHED-NOT-REBOOTED-2026-10-09.md; phase JSON excerpts |
| Recovery boot | AX80-RECOVERY-FIRSTBOOT-SUCCESS-2026-10-09.md |
| Production boot | AX80-PRODUCTION-SUCCESS-2026-10-09.md |
| Reboot persistence and final limits | Final device audit and persistence report; original public report |
| WPS window and hostapd replacement issue | AX80-WPS-USB-2026-10-09.md |
| Late image size/headroom, not flashed | Donor rebuild records; current firmware-build memory note |
| Rebase/build/PATH failure, clean env limitation | upstream-pr/REPORT.md, LOCAL-PATCHES.md, build logs/config and independent verifier |

All published source exports have a [machine-readable manifest](../evidence/source-manifest.json). Local-only source-list in the task completion record additionally lists read context notes and docs that were not copied. Old owner-specific filenames are not exposed as personal attribution. Private inputs remain private.

Public references: [PR #21640](https://github.com/openwrt/openwrt/pull/21640), [posted comment](https://github.com/openwrt/openwrt/pull/21640#issuecomment-6175000087), [PR #19440](https://github.com/openwrt/openwrt/pull/19440), [forum topic 242149](https://forum.openwrt.org/t/242149), [E8450/RT3200 conceptual installer](https://github.com/dangowrt/owrt-ubi-installer). Reading these links does not license private binary redistribution and does not turn another board's files into AX80 files.

On preparation date the PR page was readable. The forum fetch failed, so forum content was checked from saved local records; live forum availability and exact current text were not independently established. This repository asserts no current release-support or merged-PR status.
