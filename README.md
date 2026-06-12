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
Generated: 2026-06-12T23:24:57.641588+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0394s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1078s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0743s | +0.0029s | worse |
| `lteNRRCC` | 0.1207s | 0.1187s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 21.4% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0346s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0969s | 0.0931s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0669s | 0.0654s | +0.0015s | worse |
| `lteNRRCC` | 0.1184s | 0.1250s | -0.0066s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 35.07 MB | 86.4% | 107.7% |
| `f1ap_rel18.6_specs` | 22.40 MB | 103.40 MB | 107.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.73 MB | 74.05 MB | 113.6% | 104.8% |
| `lteNRRCC` | 48.14 MB | 66.09 MB | 105.4% | 104.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0346s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0937s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0688s | 0.0652s | +0.0036s | worse |
| `lteNRRCC` | 0.1309s | 0.1274s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.43 MB | 55.40 MB | 83.3% | 110.3% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.49 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.19 MB | 117.77 MB | 107.4% | 108.9% |
| `lteNRRCC` | 74.83 MB | 102.89 MB | 106.2% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0327s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.0689s | 0.0826s | -0.0137s | improved |
| `ngap_rel18.6_specs` | 0.0489s | 0.0459s | +0.0030s | worse |
| `lteNRRCC` | 0.0774s | 0.0804s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.20 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.02 MB | 3.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 5.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.00 MB | 4.67 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0422s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1130s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0753s | 0.0819s | -0.0066s | improved |
| `lteNRRCC` | 0.1401s | 0.1426s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.51 MB | 155.6% | 176.4% |
| `f1ap_rel18.6_specs` | 8.41 MB | 8.48 MB | 160.6% | 99.7% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.05 MB | 77.1% | 87.8% |
| `lteNRRCC` | 51.55 MB | 51.08 MB | 105.9% | 110.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0440s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1229s | 0.1227s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0884s | 0.0844s | +0.0040s | worse |
| `lteNRRCC` | 0.1329s | 0.1311s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.94 MB | 8.87 MB | 165.1% | 83.3% |
| `f1ap_rel18.6_specs` | 10.25 MB | 10.45 MB | 163.3% | 110.9% |
| `ngap_rel18.6_specs` | 9.48 MB | 10.26 MB | 83.7% | 119.3% |
| `lteNRRCC` | 8.90 MB | 99.45 MB | 82.5% | 118.4% |
<!-- BENCH_RESULTS_END -->
