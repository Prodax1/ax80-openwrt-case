# Historical scripts and local publication check

`history/*.txt` are archived source texts actually used in the recorded build/migration/check phases. The `.txt` suffix is deliberate: these are not executable installers. Private transport pins, address literals, individual payload pins and machine paths were removed. Their private inputs and some transport/build helpers are absent. Restoring placeholders is not enough to make a valid migration kit.

| Archive family | Role and when it ran |
| --- | --- |
| build_bootchain, build_custom, build_recovery | October offline compilation; paths and dependency tree are historical |
| prepare_factory, prepare_seeded_env_ubi, prepare_ubi_offline_candidate | Offline device-specific payload construction; no outputs distributed |
| prepare_reference_diagnostic, prepare_reference_migration | Diagnostic and writable RAM image preparation |
| execute_kernel_reserve_stage_a, execute_diagnostic_stage_b | Earlier old-layout kernel-volume resize and diagnostic update |
| execute_stock_to_reference, execute_reference_to_migration | Second route from restored OEM through official RAM to migration RAM |
| execute_approved_phase | Separately gated factory/UBI/BL2 writes and readback; no reboot in these phases |
| fix_envtools_config | Correct envtools for the installed custom UBI layout |
| upstream-build, upstream-resume-build | Clean October 13 compilation and PATH repair |
| upstream-resolve-conflict | Preserve fresh main board entries while adding AX80 |
| upstream-collect-artifacts, upstream-verify-completed-build | Artifact capture and independent offline validation |

The live script here is `check_publication.py`. Run `python scripts/check_publication.py --self-test`, then `python scripts/check_publication.py`. It reads local text and git history only, makes no network request and never connects to a router. Failures print categories/filenames, never matched values. The report inventory covers every public file; regex cannot establish legal permission or prove the absence of every imaginable secret.

Do not use the archived SSH/mutation code as a current operation. Consult provenance and license status before copying code into another project.
