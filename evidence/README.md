# Evidence: selected excerpts, not full device logs

| File | What it supports | What it does not prove |
| --- | --- | --- |
| migration-status.json; migration-*.log | Three recorded phases PASS, commands/exit codes, no reboot during writes | Boot of the new chain or atomic rollback |
| installed-boot-and-storage.log | Board/kernel and internal filesystem observations from saved audit | Current reachability, client traffic or new image boot |
| build-path-failure.log | Shell syntax failure in first build | A source-code defect |
| rebased-build-result.txt | Saved successful make result | Hardware suitability |
| rebased-verification.json/.log, rebased-fip.txt | Offline artifact verifier and FIP structure | Hardware boot or cryptographic authenticity |
| rebased-uboot-env.txt | Clean generated loader config lacks redundant backend | Correctness of any future patch |
| platform-resolution.diff; range-diff.txt | Scope of manual rebase conflict resolution | Remote CI approval or merge |
| firmware-sha256.json | Locally recomputed size/hash for 18 firmware files | Permission to redistribute old proprietary-containing images |
| source-manifest.json | Source-to-export mapping and transformations | Complete original private dataset |

Command text is preserved except removed private paths/identifiers. Readback values for factory, device env, full NAND and host keys are not published; only equality/status is described. Trimming is explicit: these excerpts omit identities, networks, keys, Wi-Fi settings and unrelated service logs. They do not claim that the current local task repeated hardware tests. [Source notes](../docs/sources.md) connect observations to the historical checkpoints.
