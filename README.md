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
Generated: 2026-11-10T04:00:45.352091+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0394s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1208s | 0.1204s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0847s | 0.0835s | +0.0012s | worse |
| `lteNRRCC` | 0.1262s | 0.1272s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 10.8% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.2% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 101.9% |
| `lteNRRCC` | 72.41 MB | 100.18 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0314s | 0.0374s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0991s | 0.1084s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0682s | 0.0745s | -0.0063s | improved |
| `lteNRRCC` | 0.0988s | 0.1176s | -0.0188s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.84 MB | 34.65 MB | 69.6% | 104.2% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 104.2% | 101.8% |
| `ngap_rel18.6_specs` | 18.06 MB | 72.65 MB | 105.3% | 104.8% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.1% | 103.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0549s | -0.0174s | improved |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1689s | -0.0541s | improved |
| `ngap_rel18.6_specs` | 0.0812s | 0.1157s | -0.0345s | improved |
| `lteNRRCC` | 0.1076s | 0.1631s | -0.0555s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.81 MB | 53.73 MB | 69.6% | 107.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 104.2% | 101.5% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 110.5% | 102.0% |
| `lteNRRCC` | 72.58 MB | 100.36 MB | 102.1% | 101.7% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0341s | +0.0074s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.0935s | +0.0193s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0658s | +0.0119s | worse |
| `lteNRRCC` | 0.1417s | 0.1127s | +0.0290s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 7.44 MB | 0.0% | 157.7% |
| `f1ap_rel18.6_specs` | 8.62 MB | 8.12 MB | 137.9% | 79.7% |
| `ngap_rel18.6_specs` | 7.34 MB | 7.69 MB | 110.7% | 156.3% |
| `lteNRRCC` | 51.10 MB | 52.52 MB | 157.1% | 154.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0357s | +0.0060s | worse |
| `f1ap_rel18.6_specs` | 0.1179s | 0.1017s | +0.0162s | worse |
| `ngap_rel18.6_specs` | 0.0831s | 0.0694s | +0.0137s | worse |
| `lteNRRCC` | 0.1361s | 0.1120s | +0.0241s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 9.09 MB | 0.0% | 144.4% |
| `f1ap_rel18.6_specs` | 9.88 MB | 164.21 MB | 150.6% | 104.9% |
| `ngap_rel18.6_specs` | 10.47 MB | 9.22 MB | 104.5% | 98.6% |
| `lteNRRCC` | 8.95 MB | 97.84 MB | 108.1% | 107.8% |
<!-- BENCH_RESULTS_END -->
