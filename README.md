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
Generated: 2026-10-19T16:53:25.562337+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0344s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1097s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0749s | +0.0023s | worse |
| `lteNRRCC` | 0.1217s | 0.1224s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 14.7% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0219s | 0.0343s | -0.0124s | improved |
| `f1ap_rel18.6_specs` | 0.0605s | 0.0961s | -0.0356s | improved |
| `ngap_rel18.6_specs` | 0.0417s | 0.0670s | -0.0253s | improved |
| `lteNRRCC` | 0.0766s | 0.1296s | -0.0530s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.62 MB | 77.8% | 105.6% |
| `f1ap_rel18.6_specs` | 21.81 MB | 102.98 MB | 100.0% | 102.7% |
| `ngap_rel18.6_specs` | 18.12 MB | 74.56 MB | 112.5% | 103.6% |
| `lteNRRCC` | 48.70 MB | 66.16 MB | 102.5% | 102.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0284s | 0.0352s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0771s | 0.0906s | -0.0135s | improved |
| `ngap_rel18.6_specs` | 0.0534s | 0.0618s | -0.0084s | improved |
| `lteNRRCC` | 0.1025s | 0.1168s | -0.0143s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 55.83 MB | 68.0% | 104.5% |
| `f1ap_rel18.6_specs` | 34.70 MB | 164.42 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 24.26 MB | 117.47 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.40 MB | 102.93 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0262s | 0.0237s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0793s | +0.0139s | worse |
| `ngap_rel18.6_specs` | 0.0645s | 0.0467s | +0.0178s | worse |
| `lteNRRCC` | 0.1040s | 0.0774s | +0.0266s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.91 MB | 4.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.97 MB | 5.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.11 MB | 3.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.77 MB | 4.70 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0282s | 0.0390s | -0.0108s | improved |
| `f1ap_rel18.6_specs` | 0.0781s | 0.1087s | -0.0306s | improved |
| `ngap_rel18.6_specs` | 0.0599s | 0.0750s | -0.0151s | improved |
| `lteNRRCC` | 0.0919s | 0.1402s | -0.0483s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.31 MB | 8.91 MB | 0.0% | 143.5% |
| `f1ap_rel18.6_specs` | 9.55 MB | 9.61 MB | 222.6% | 137.0% |
| `ngap_rel18.6_specs` | 9.12 MB | 9.03 MB | 221.8% | 148.1% |
| `lteNRRCC` | 8.78 MB | 70.52 MB | 148.1% | 233.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0447s | -0.0058s | improved |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1294s | -0.0154s | improved |
| `ngap_rel18.6_specs` | 0.0774s | 0.0884s | -0.0110s | improved |
| `lteNRRCC` | 0.1308s | 0.1325s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.12 MB | 8.91 MB | 0.0% | 164.8% |
| `f1ap_rel18.6_specs` | 10.14 MB | 11.80 MB | 151.8% | 102.9% |
| `ngap_rel18.6_specs` | 9.22 MB | 9.18 MB | 152.5% | 159.2% |
| `lteNRRCC` | 8.78 MB | 87.23 MB | 143.7% | 147.6% |
<!-- BENCH_RESULTS_END -->
