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
Generated: 2026-10-17T13:33:52.860147+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0346s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1091s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0745s | 0.0751s | -0.0006s | improved |
| `lteNRRCC` | 0.1179s | 0.1182s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 18.6% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0291s | +0.0076s | worse |
| `f1ap_rel18.6_specs` | 0.0929s | 0.0765s | +0.0164s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0530s | +0.0127s | worse |
| `lteNRRCC` | 0.1288s | 0.0999s | +0.0289s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 35.97 MB | 19.1% | 107.7% |
| `f1ap_rel18.6_specs` | 21.72 MB | 103.20 MB | 106.7% | 103.6% |
| `ngap_rel18.6_specs` | 18.01 MB | 74.38 MB | 108.3% | 102.4% |
| `lteNRRCC` | 48.30 MB | 66.18 MB | 103.2% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0221s | 0.0338s | -0.0117s | improved |
| `f1ap_rel18.6_specs` | 0.0639s | 0.0891s | -0.0252s | improved |
| `ngap_rel18.6_specs` | 0.0439s | 0.0619s | -0.0180s | improved |
| `lteNRRCC` | 0.0781s | 0.1150s | -0.0369s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 55.56 MB | 70.0% | 105.6% |
| `f1ap_rel18.6_specs` | 34.67 MB | 164.49 MB | 105.3% | 102.6% |
| `ngap_rel18.6_specs` | 23.74 MB | 117.27 MB | 106.2% | 100.0% |
| `lteNRRCC` | 74.23 MB | 102.54 MB | 102.7% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0542s | 0.0421s | +0.0121s | worse |
| `f1ap_rel18.6_specs` | 0.0642s | 0.0729s | -0.0087s | improved |
| `ngap_rel18.6_specs` | 0.0529s | 0.0563s | -0.0034s | improved |
| `lteNRRCC` | 0.1020s | 0.0986s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.67 MB | 5.59 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.06 MB | 8.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.20 MB | 8.33 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.42 MB | 5.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0342s | +0.0077s | worse |
| `f1ap_rel18.6_specs` | 0.1195s | 0.0986s | +0.0209s | worse |
| `ngap_rel18.6_specs` | 0.0822s | 0.0728s | +0.0094s | worse |
| `lteNRRCC` | 0.1304s | 0.1173s | +0.0131s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.28 MB | 8.27 MB | 0.0% | 152.7% |
| `f1ap_rel18.6_specs` | 8.89 MB | 106.62 MB | 153.4% | 109.4% |
| `ngap_rel18.6_specs` | 8.40 MB | 9.27 MB | 153.1% | 128.0% |
| `lteNRRCC` | 8.64 MB | 51.97 MB | 76.4% | 110.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0418s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.1044s | 0.1140s | -0.0096s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0823s | -0.0057s | improved |
| `lteNRRCC` | 0.1138s | 0.1286s | -0.0148s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.25 MB | 0.0% | 124.8% |
| `f1ap_rel18.6_specs` | 11.06 MB | 162.77 MB | 139.5% | 138.2% |
| `ngap_rel18.6_specs` | 10.36 MB | 10.80 MB | 115.0% | 133.2% |
| `lteNRRCC` | 9.41 MB | 95.75 MB | 138.8% | 134.9% |
<!-- BENCH_RESULTS_END -->
