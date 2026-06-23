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
Generated: 2026-06-23T12:39:59.365968+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0352s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1102s | 0.1108s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0751s | +0.0006s | worse |
| `lteNRRCC` | 0.1188s | 0.1190s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 20.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0360s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0942s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0695s | 0.0661s | +0.0034s | worse |
| `lteNRRCC` | 0.1272s | 0.1239s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 36.52 MB | 100.0% | 113.8% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.23 MB | 109.1% | 104.9% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.45 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.49 MB | 66.49 MB | 104.8% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0361s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0883s | 0.0944s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0616s | 0.0670s | -0.0054s | improved |
| `lteNRRCC` | 0.1154s | 0.1280s | -0.0126s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 54.68 MB | 84.0% | 111.5% |
| `f1ap_rel18.6_specs` | 34.74 MB | 164.69 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.71 MB | 112.5% | 104.9% |
| `lteNRRCC` | 75.01 MB | 102.84 MB | 105.3% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0390s | -0.0184s | improved |
| `f1ap_rel18.6_specs` | 0.0620s | 0.1262s | -0.0642s | improved |
| `ngap_rel18.6_specs` | 0.0476s | 0.0847s | -0.0371s | improved |
| `lteNRRCC` | 0.0755s | 0.1282s | -0.0527s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.23 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.66 MB | 3.72 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.44 MB | 4.73 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.67 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0410s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1095s | 0.1133s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0798s | -0.0028s | improved |
| `lteNRRCC` | 0.1399s | 0.1321s | +0.0078s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.50 MB | 100.0% | 158.2% |
| `f1ap_rel18.6_specs` | 8.11 MB | 106.64 MB | 157.6% | 107.3% |
| `ngap_rel18.6_specs` | 7.87 MB | 7.95 MB | 172.5% | 155.2% |
| `lteNRRCC` | 8.16 MB | 69.30 MB | 157.4% | 154.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0378s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1126s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0776s | +0.0003s | worse |
| `lteNRRCC` | 0.1242s | 0.1295s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.02 MB | 10.66 MB | 153.2% | 108.9% |
| `f1ap_rel18.6_specs` | 11.59 MB | 164.20 MB | 213.7% | 160.4% |
| `ngap_rel18.6_specs` | 9.19 MB | 9.42 MB | 150.8% | 151.8% |
| `lteNRRCC` | 8.57 MB | 98.59 MB | 153.0% | 106.4% |
<!-- BENCH_RESULTS_END -->
