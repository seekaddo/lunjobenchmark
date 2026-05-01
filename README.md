# lunjobenchmark

Benchmarking `voltcc` parser, syntaxcheck, and validator-adjacent phases across supported release binaries.

## Layout

- `test_semantic/`: copy of only the upstream fixtures used by the benchmark scripts, with Objective Systems generated headers removed where present
- `releases/`: release archives or extracted binaries produced from `build_release.sh`
- `preparebin.sh`: extracts the native binary for the current runner and places it where the copied benchmark scripts expect it
- `scripts/refresh_releases.sh`: rebuilds the parent repo releases and copies the fresh `releases/` tree into this repo
- `run_benchmarks.sh`: runs the copied upstream benchmark scripts and writes per-target JSON results
- `collect_benchmark_results.py`: parses the copied benchmark script logs into summary JSON
- `update_readme.py`: updates the results section from `bench_results`
- `bench_results/`: latest and historical benchmark output, including raw console logs for each benchmark suite alongside the JSON summaries

## Assumptions

- The benchmark repo has access to release archives named like `voltcc-v<version>-<target>.tar.gz`.
- `preparebin.sh` prefers `./releases/` and falls back to `../releases/` for local nested-repo development.
- The copied upstream benchmark scripts execute the prepared binary from `./zig-out/bin/voltcc`, matching the local `test_semantic` script layout.

## Latest Results

<!-- BENCH_RESULTS_START -->
Generated: 2026-05-01T11:14:14.475868+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0375s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1150s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0786s | 0.0796s | -0.0010s | improved |
| `lteNRRCC` | 0.1229s | 0.1236s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.1% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0315s | 0.0349s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0920s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0644s | +0.0008s | worse |
| `lteNRRCC` | 0.1154s | 0.1274s | -0.0120s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 36.60 MB | 20.0% | 107.7% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.49 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 16.83 MB | 74.54 MB | 113.6% | 104.9% |
| `lteNRRCC` | 48.77 MB | 66.16 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0379s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0959s | 0.0978s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0687s | -0.0025s | improved |
| `lteNRRCC` | 0.1301s | 0.1311s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 54.88 MB | 86.2% | 113.8% |
| `f1ap_rel18.6_specs` | 35.16 MB | 164.33 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.72 MB | 111.1% | 104.4% |
| `lteNRRCC` | 74.79 MB | 102.46 MB | 104.6% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0182s | 0.0196s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0674s | 0.0580s | +0.0094s | worse |
| `ngap_rel18.6_specs` | 0.0403s | 0.0403s | +0.0000s | flat |
| `lteNRRCC` | 0.0676s | 0.0701s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.42 MB | 4.44 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.03 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.08 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.66 MB | 3.69 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0389s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1119s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0751s | +0.0018s | worse |
| `lteNRRCC` | 0.1290s | 0.1369s | -0.0079s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.36 MB | 8.46 MB | 112.8% | 112.4% |
| `f1ap_rel18.6_specs` | 8.72 MB | 8.66 MB | 234.3% | 111.8% |
| `ngap_rel18.6_specs` | 8.48 MB | 8.42 MB | 230.7% | 112.7% |
| `lteNRRCC` | 8.53 MB | 69.21 MB | 114.5% | 106.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0403s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1198s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0767s | 0.0804s | -0.0037s | improved |
| `lteNRRCC` | 0.1317s | 0.1317s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 8.85 MB | 152.9% | 76.3% |
| `f1ap_rel18.6_specs` | 10.07 MB | 9.74 MB | 155.5% | 157.4% |
| `ngap_rel18.6_specs` | 9.07 MB | 9.22 MB | 81.5% | 172.8% |
| `lteNRRCC` | 9.86 MB | 80.01 MB | 226.0% | 154.8% |
<!-- BENCH_RESULTS_END -->
