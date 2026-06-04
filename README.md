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
Generated: 2026-06-04T23:14:53.533302+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0345s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1093s | 0.1074s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0746s | 0.0738s | +0.0008s | worse |
| `lteNRRCC` | 0.1182s | 0.1166s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 26.2% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0382s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0989s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0635s | 0.0697s | -0.0062s | improved |
| `lteNRRCC` | 0.1230s | 0.1313s | -0.0083s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.44 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.31 MB | 112.5% | 105.3% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.20 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.00 MB | 65.56 MB | 106.2% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0360s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0930s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0652s | +0.0014s | worse |
| `lteNRRCC` | 0.1304s | 0.1269s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.68 MB | 21.7% | 110.0% |
| `f1ap_rel18.6_specs` | 34.02 MB | 164.72 MB | 106.1% | 105.1% |
| `ngap_rel18.6_specs` | 23.96 MB | 117.61 MB | 110.7% | 108.9% |
| `lteNRRCC` | 74.44 MB | 102.92 MB | 104.6% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0212s | 0.0190s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0679s | 0.0684s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0494s | 0.0482s | +0.0012s | worse |
| `lteNRRCC` | 0.0803s | 0.0789s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.09 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 5.64 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.94 MB | 5.28 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.08 MB | 3.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0322s | 0.0400s | -0.0078s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.1132s | -0.0199s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0766s | -0.0127s | improved |
| `lteNRRCC` | 0.1115s | 0.1386s | -0.0271s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.97 MB | 7.85 MB | 141.6% | 143.6% |
| `f1ap_rel18.6_specs` | 8.43 MB | 106.64 MB | 208.1% | 140.8% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.24 MB | 140.6% | 145.5% |
| `lteNRRCC` | 8.29 MB | 61.11 MB | 142.2% | 264.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0454s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.1239s | 0.1290s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0918s | 0.0921s | -0.0003s | improved |
| `lteNRRCC` | 0.1385s | 0.1446s | -0.0061s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 9.00 MB | 170.0% | 172.4% |
| `f1ap_rel18.6_specs` | 10.05 MB | 164.18 MB | 165.5% | 167.4% |
| `ngap_rel18.6_specs` | 9.92 MB | 9.20 MB | 106.3% | 83.2% |
| `lteNRRCC` | 8.73 MB | 74.14 MB | 82.4% | 104.2% |
<!-- BENCH_RESULTS_END -->
