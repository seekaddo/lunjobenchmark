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
Generated: 2026-10-10T01:37:03.384851+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0357s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1117s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0762s | -0.0017s | improved |
| `lteNRRCC` | 0.1178s | 0.1203s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.88 MB | 53.55 MB | 68.0% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.4% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0277s | +0.0062s | worse |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0757s | +0.0148s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0526s | +0.0103s | worse |
| `lteNRRCC` | 0.1230s | 0.0976s | +0.0254s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.18 MB | 80.0% | 107.7% |
| `f1ap_rel18.6_specs` | 22.41 MB | 103.42 MB | 103.2% | 103.7% |
| `ngap_rel18.6_specs` | 18.01 MB | 74.58 MB | 104.0% | 102.4% |
| `lteNRRCC` | 48.47 MB | 66.47 MB | 101.7% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0232s | 0.0341s | -0.0109s | improved |
| `f1ap_rel18.6_specs` | 0.0604s | 0.0917s | -0.0313s | improved |
| `ngap_rel18.6_specs` | 0.0404s | 0.0633s | -0.0229s | improved |
| `lteNRRCC` | 0.0749s | 0.1170s | -0.0421s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.70 MB | 55.89 MB | 59.1% | 105.9% |
| `f1ap_rel18.6_specs` | 34.46 MB | 164.54 MB | 105.6% | 102.9% |
| `ngap_rel18.6_specs` | 24.29 MB | 117.66 MB | 106.7% | 103.8% |
| `lteNRRCC` | 74.94 MB | 102.78 MB | 102.8% | 102.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0223s | 0.0261s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1031s | 0.0789s | +0.0242s | worse |
| `ngap_rel18.6_specs` | 0.0868s | 0.0832s | +0.0036s | worse |
| `lteNRRCC` | 0.1268s | 0.0833s | +0.0435s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.59 MB | 7.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.08 MB | 9.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.92 MB | 10.03 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.14 MB | 7.22 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0289s | 0.0336s | -0.0047s | improved |
| `f1ap_rel18.6_specs` | 0.0860s | 0.0947s | -0.0087s | improved |
| `ngap_rel18.6_specs` | 0.0574s | 0.0665s | -0.0091s | improved |
| `lteNRRCC` | 0.0931s | 0.1120s | -0.0189s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 15.65 MB | 0.0% | 153.5% |
| `f1ap_rel18.6_specs` | 20.61 MB | 12.84 MB | 120.5% | 100.1% |
| `ngap_rel18.6_specs` | 16.32 MB | 16.88 MB | 148.8% | 131.8% |
| `lteNRRCC` | 9.08 MB | 28.88 MB | 137.2% | 125.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0489s | 0.0405s | +0.0084s | worse |
| `f1ap_rel18.6_specs` | 0.1422s | 0.1169s | +0.0253s | worse |
| `ngap_rel18.6_specs` | 0.0985s | 0.0816s | +0.0169s | worse |
| `lteNRRCC` | 0.1395s | 0.1313s | +0.0082s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.76 MB | 10.18 MB | 0.0% | 222.1% |
| `f1ap_rel18.6_specs` | 10.12 MB | 164.17 MB | 77.0% | 157.4% |
| `ngap_rel18.6_specs` | 10.29 MB | 10.23 MB | 80.1% | 220.2% |
| `lteNRRCC` | 69.45 MB | 99.74 MB | 200.2% | 156.0% |
<!-- BENCH_RESULTS_END -->
