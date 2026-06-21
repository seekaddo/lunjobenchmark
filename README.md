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
Generated: 2026-06-21T12:13:31.824471+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0352s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1142s | 0.1092s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0765s | 0.0748s | +0.0017s | worse |
| `lteNRRCC` | 0.1219s | 0.1192s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.67 MB | 53.55 MB | 7.3% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0346s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0985s | 0.0938s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0706s | 0.0656s | +0.0050s | worse |
| `lteNRRCC` | 0.1333s | 0.1306s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.70 MB | 88.9% | 110.3% |
| `f1ap_rel18.6_specs` | 21.64 MB | 103.46 MB | 109.4% | 103.4% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.71 MB | 111.1% | 106.7% |
| `lteNRRCC` | 47.53 MB | 65.85 MB | 103.1% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0365s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0955s | 0.0947s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0657s | +0.0018s | worse |
| `lteNRRCC` | 0.1294s | 0.1280s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.79 MB | 100.0% | 110.3% |
| `f1ap_rel18.6_specs` | 34.56 MB | 164.28 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.81 MB | 111.5% | 106.7% |
| `lteNRRCC` | 74.74 MB | 102.65 MB | 104.8% | 103.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0288s | 0.0252s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.0603s | 0.0680s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0402s | 0.0479s | -0.0077s | improved |
| `lteNRRCC` | 0.0669s | 0.0816s | -0.0147s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.38 MB | 8.06 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.31 MB | 4.55 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.19 MB | 4.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.69 MB | 7.17 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0400s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.0946s | 0.1100s | -0.0154s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0779s | -0.0127s | improved |
| `lteNRRCC` | 0.1125s | 0.1471s | -0.0346s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.81 MB | 143.2% | 0.0% |
| `f1ap_rel18.6_specs` | 8.43 MB | 106.64 MB | 138.4% | 139.8% |
| `ngap_rel18.6_specs` | 8.37 MB | 8.24 MB | 141.3% | 139.6% |
| `lteNRRCC` | 8.61 MB | 50.88 MB | 140.1% | 124.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0407s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1263s | 0.1271s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0798s | 0.0814s | -0.0016s | improved |
| `lteNRRCC` | 0.1307s | 0.1445s | -0.0138s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.56 MB | 10.65 MB | 102.4% | 224.6% |
| `f1ap_rel18.6_specs` | 9.56 MB | 9.49 MB | 157.4% | 80.7% |
| `ngap_rel18.6_specs` | 9.02 MB | 8.96 MB | 157.5% | 157.3% |
| `lteNRRCC` | 8.62 MB | 101.71 MB | 156.3% | 153.4% |
<!-- BENCH_RESULTS_END -->
