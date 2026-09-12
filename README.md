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
Generated: 2026-09-12T00:02:45.254386+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0364s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1099s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0754s | -0.0010s | improved |
| `lteNRRCC` | 0.1184s | 0.1204s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 77.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 100.0% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0261s | 0.0336s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.0723s | 0.0901s | -0.0178s | improved |
| `ngap_rel18.6_specs` | 0.0507s | 0.0639s | -0.0132s | improved |
| `lteNRRCC` | 0.0963s | 0.1236s | -0.0273s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.45 MB | 80.0% | 104.8% |
| `f1ap_rel18.6_specs` | 22.06 MB | 103.34 MB | 104.2% | 100.0% |
| `ngap_rel18.6_specs` | 18.05 MB | 74.70 MB | 105.0% | 106.1% |
| `lteNRRCC` | 48.55 MB | 66.29 MB | 102.1% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0323s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0910s | 0.0893s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0631s | 0.0617s | +0.0014s | worse |
| `lteNRRCC` | 0.1176s | 0.1146s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.53 MB | 55.66 MB | 76.0% | 107.7% |
| `f1ap_rel18.6_specs` | 34.64 MB | 164.25 MB | 103.6% | 103.6% |
| `ngap_rel18.6_specs` | 24.51 MB | 116.97 MB | 108.7% | 104.9% |
| `lteNRRCC` | 74.77 MB | 102.79 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0309s | +0.0092s | worse |
| `f1ap_rel18.6_specs` | 0.0718s | 0.0813s | -0.0095s | improved |
| `ngap_rel18.6_specs` | 0.0690s | 0.0516s | +0.0174s | worse |
| `lteNRRCC` | 0.1065s | 0.0934s | +0.0131s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.59 MB | 9.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.61 MB | 7.20 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.20 MB | 5.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.97 MB | 3.89 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0257s | 0.0403s | -0.0146s | improved |
| `f1ap_rel18.6_specs` | 0.0738s | 0.1085s | -0.0347s | improved |
| `ngap_rel18.6_specs` | 0.0538s | 0.0780s | -0.0242s | improved |
| `lteNRRCC` | 0.0839s | 0.1376s | -0.0537s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 34.85 MB | 0.0% | 131.6% |
| `f1ap_rel18.6_specs` | 10.87 MB | 19.77 MB | 130.1% | 135.9% |
| `ngap_rel18.6_specs` | 9.30 MB | 16.80 MB | 148.5% | 149.5% |
| `lteNRRCC` | 18.68 MB | 14.17 MB | 126.9% | 82.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0382s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1077s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0752s | 0.0743s | +0.0009s | worse |
| `lteNRRCC` | 0.1270s | 0.1244s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.68 MB | 8.57 MB | 107.3% | 174.5% |
| `f1ap_rel18.6_specs` | 10.02 MB | 9.58 MB | 157.8% | 162.0% |
| `ngap_rel18.6_specs` | 11.02 MB | 8.91 MB | 223.8% | 159.7% |
| `lteNRRCC` | 8.58 MB | 72.20 MB | 158.0% | 154.2% |
<!-- BENCH_RESULTS_END -->
