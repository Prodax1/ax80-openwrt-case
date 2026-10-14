# SANITIZE-REPORT — local publication review

Prepared 2026-10-14. No push, PR, issue, comment, SSH, context write or sync was performed in this task. The first rules read mistakenly displayed service addresses/private owner labels in the task tool output; those are not included in this public repository. Subsequent memory reads suppressed credential-related lines. This report never repeats matched values.

## Selection and redactions

Only reviewed text sources were exported. Full private logs, NAND/factory/ART/calibration dumps, full flash backups, config backups, VPN/mihomo/SSClash server configs, proprietary binaries, personal screenshots, keys and all firmware binaries were excluded. Device-specific factory/env/full-flash hashes were excluded as identifying data. Firmware SHA256 is an inventory of generic image files, not a dump inventory or permission to distribute proprietary-containing images.

| Detected source category | Replacements in selected exports | Treatment |
| --- | ---: | --- |
| UUID | 1 | Placeholder or entire credential-related line removed |
| credential-related line | 2 | Placeholder or entire credential-related line removed |
| historical pinned hashes | 5 | Placeholder or entire credential-related line removed |
| host fingerprint | 1 | Placeholder or entire credential-related line removed |
| network address | 29 | Placeholder or entire credential-related line removed |
| private path | 41 | Placeholder or entire credential-related line removed |
| terminal control characters | 68 | Placeholder or entire credential-related line removed |

Private router owners are unnamed. Public upstream author attribution and the requested public links remain intentionally. The original public README is retained byte for byte as docs/original-report.md; its Publication boundaries section is also retained in the new English README. No logos, theme files or existing legal text were edited. LICENSE is the GNU GPL v2.0 text (owner decision 2026-10-14, same as OpenWrt); imported upstream material keeps its in-file notices, see ATTRIBUTION.md.

## Automatic checks and actual output

Commands (run locally, no transport code executed):

```sh
python scripts/check_publication.py --self-test
python scripts/check_publication.py
git grep --cached -I -l -E <pattern embedded in scripts/check_publication.py>
```

The complete executable regex is embedded in the checker, avoiding a shell-dependent copy here. Python inspects every public file for IPv4, IPv6, MAC, UUID, host fingerprints, token formats, credential/SSID/serial/HWID assignments, key constants, private paths, unapproved URL domains, bare infrastructure-looking domains, forbidden artifacts and non-text files. git grep independently searches the index using POSIX ERE and prints only filenames if it finds a match. Every reachable historical blob is also scanned.

Self-test output:

```json
{"self_test":"PASS","positive_categories":14,"git_grep_positive_and_negative":"PASS"}
```

Both git grep controls used the same staged-file flags and pattern as the real scan: known matching fixture exit 0 with filename, clean fixture exit 1 with no filename. Real staged git grep exit 1 with no matches. Thus no-match is backed by a working positive control, not confused with tool failure. Python checks similarly detected fixtures for all 14 categories.

First export check found one remaining machine path in the historical envtools helper, which was replaced. Two self-check source literals caused false positives; fixture construction/pattern spelling was corrected without disabling the detectors. Final result: PASS, no categories detected, no non-text/forbidden files. The complete per-file inventory is below. The check was repeated after local commits to cover newly reachable blobs.

Other local verification: Markdown file links resolve; no disallowed control characters; saved original report and retained legal boundary match. git diff --check is clean for new narratives/checker/metadata. Historical source/config/patch excerpts retain original whitespace where present; locations are recorded below rather than silently rewriting upstream content.

## Scope limits

Regex screening is heuristic: it cannot prove no unknown secret is encoded, validate redistribution rights, or replace human review. No hardware behavior was retested. A compiled/hashed artifact is not a ready-to-flash image. The live forum page fetch failed; its current text/availability was not verified. Credentials/values are absent from this report; finding counts are per exported occurrence, not unique secret counts.

## Files checked

The report itself is included in the final rerun; its row is marked self-report because its byte count changes with this inventory.

| Public file | Bytes at scan | Result |
| --- | ---: | --- |
| `.gitignore` | 81 | PASS |
| `ATTRIBUTION.md` | 1608 | PASS |
| `configs/installed-era/custom-01.config` | 297893 | PASS |
| `configs/installed-era/custom-01.config.diff` | 6862 | PASS |
| `configs/installed-era/recovery-02.config` | 277306 | PASS |
| `configs/installed-era/recovery-02.config.diff` | 751 | PASS |
| `configs/installed-era/uboot-candidate04.config` | 43667 | PASS |
| `configs/README.md` | 1131 | PASS |
| `configs/rebased/build.config` | 186449 | PASS |
| `configs/rebased/diffconfig` | 1410 | PASS |
| `configs/rebased/feeds.buildinfo` | 193 | PASS |
| `docs/01-preparation.md` | 4230 | PASS |
| `docs/02-stock-and-initramfs.md` | 5033 | PASS |
| `docs/03-bootchain-and-ubi.md` | 5628 | PASS |
| `docs/04-verification.md` | 4216 | PASS |
| `docs/05-recovery-and-rollback.md` | 4161 | PASS |
| `docs/06-upstream-build.md` | 4581 | PASS |
| `docs/glossary.md` | 3456 | PASS |
| `docs/original-report.md` | 7385 | PASS |
| `docs/README.md` | 1580 | PASS |
| `docs/sources.md` | 2629 | PASS |
| `evidence/build-path-failure.log` | 114 | PASS |
| `evidence/firmware-sha256.json` | 4293 | PASS |
| `evidence/installed-boot-and-storage.log` | 2514 | PASS |
| `evidence/migration-bl2.log` | 612 | PASS |
| `evidence/migration-factory.log` | 351 | PASS |
| `evidence/migration-status.json` | 220 | PASS |
| `evidence/migration-ubi.log` | 1075 | PASS |
| `evidence/platform-resolution.diff` | 943 | PASS |
| `evidence/range-diff.txt` | 2451 | PASS |
| `evidence/README.md` | 1707 | PASS |
| `evidence/rebased-build-result.txt` | 45 | PASS |
| `evidence/rebased-fip.txt` | 146 | PASS |
| `evidence/rebased-uboot-env.txt` | 398 | PASS |
| `evidence/rebased-verification.json` | 409 | PASS |
| `evidence/rebased-verification.log` | 460 | PASS |
| `evidence/source-manifest.json` | 14015 | PASS |
| `LICENSE` | 17984 | PASS |
| `patches/local/awg-crypto-select.patch` | 315 | PASS |
| `patches/local/env-redundant-port-fix.patch` | 360 | PASS |
| `patches/local/hardened-env.patch` | 4639 | PASS |
| `patches/local/ram-uboot-no-nand.patch` | 316 | PASS |
| `patches/local/recovery-no-bootloader.patch` | 609 | PASS |
| `patches/README.md` | 1863 | PASS |
| `patches/upstream/ax80-eu-ubi-rebased.diff` | 33101 | PASS |
| `patches/upstream/pr21640-original.diff` | 33120 | PASS |
| `README.md` | 6742 | PASS |
| `README.ru.md` | 10355 | PASS |
| `RELEASES.md` | 4449 | PASS |
| `SANITIZE-REPORT.md` | 10313 | PASS |
| `scripts/check_publication.py` | 7069 | PASS |
| `scripts/history/ax80-enable-telnet.py.txt` | 3898 | PASS |
| `scripts/history/ax80-telnet-backup.py.txt` | 9540 | PASS |
| `scripts/history/ax80-verify-backups.py.txt` | 3172 | PASS |
| `scripts/history/build_bootchain.sh.txt` | 3210 | PASS |
| `scripts/history/build_custom.sh.txt` | 1039 | PASS |
| `scripts/history/build_recovery.sh.txt` | 1115 | PASS |
| `scripts/history/execute_approved_phase.py.txt` | 9752 | PASS |
| `scripts/history/execute_diagnostic_stage_b.py.txt` | 6600 | PASS |
| `scripts/history/execute_kernel_reserve_stage_a.py.txt` | 8219 | PASS |
| `scripts/history/execute_reference_to_migration.py.txt` | 7271 | PASS |
| `scripts/history/execute_stock_to_reference.py.txt` | 5308 | PASS |
| `scripts/history/fix_envtools_config.py.txt` | 2544 | PASS |
| `scripts/history/prepare_factory.py.txt` | 3608 | PASS |
| `scripts/history/prepare_reference_diagnostic.py.txt` | 14417 | PASS |
| `scripts/history/prepare_reference_migration.py.txt` | 7234 | PASS |
| `scripts/history/prepare_seeded_env_ubi.py.txt` | 7219 | PASS |
| `scripts/history/prepare_ubi_offline_candidate.py.txt` | 6050 | PASS |
| `scripts/history/upstream-build.sh.txt` | 2105 | PASS |
| `scripts/history/upstream-collect-artifacts.py.txt` | 4808 | PASS |
| `scripts/history/upstream-resolve-conflict.py.txt` | 886 | PASS |
| `scripts/history/upstream-resume-build.sh.txt` | 970 | PASS |
| `scripts/history/upstream-verify-completed-build.py.txt` | 6533 | PASS |
| `scripts/README.md` | 2218 | PASS |
| `SANITIZE-REPORT.md` | self-report | PASS on final rerun |

## Retained source whitespace

- `evidence/platform-resolution.diff` — 15 retained whitespace locations (patch context, historical source or generated Kconfig). Full locations can be reproduced with git diff --check against the baseline.
- `evidence/range-diff.txt` — 12 retained whitespace locations (patch context, historical source or generated Kconfig). Full locations can be reproduced with git diff --check against the baseline.
- `patches/local/awg-crypto-select.patch` — 6 retained whitespace locations (patch context, historical source or generated Kconfig). Full locations can be reproduced with git diff --check against the baseline.
- `patches/local/ram-uboot-no-nand.patch` — 1 retained whitespace locations (patch context, historical source or generated Kconfig). Full locations can be reproduced with git diff --check against the baseline.
- `patches/upstream/ax80-eu-ubi-rebased.diff` — 44 retained whitespace locations (patch context, historical source or generated Kconfig). Full locations can be reproduced with git diff --check against the baseline.
- `patches/upstream/pr21640-original.diff` — 44 retained whitespace locations (patch context, historical source or generated Kconfig). Full locations can be reproduced with git diff --check against the baseline.
- `scripts/history/upstream-resolve-conflict.py.txt` — 2 retained whitespace locations (patch context, historical source or generated Kconfig). Full locations can be reproduced with git diff --check against the baseline.