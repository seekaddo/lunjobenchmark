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
Generated: 2026-10-01T01:11:19.425165+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0367s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1151s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0802s | 0.0784s | +0.0018s | worse |
| `lteNRRCC` | 0.1221s | 0.1243s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 87.0% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0235s | +0.0122s | worse |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0675s | +0.0256s | worse |
| `ngap_rel18.6_specs` | 0.0655s | 0.0422s | +0.0233s | worse |
| `lteNRRCC` | 0.1289s | 0.0865s | +0.0424s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 36.22 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.40 MB | 103.32 MB | 103.2% | 100.0% |
| `ngap_rel18.6_specs` | 17.89 MB | 73.75 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.80 MB | 66.23 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0381s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.1043s | -0.0101s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0693s | -0.0039s | improved |
| `lteNRRCC` | 0.1289s | 0.1230s | +0.0059s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.20 MB | 80.8% | 103.6% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.54 MB | 106.7% | 103.5% |
| `ngap_rel18.6_specs` | 24.20 MB | 117.63 MB | 108.0% | 102.3% |
| `lteNRRCC` | 74.98 MB | 102.46 MB | 101.6% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0312s | 0.0494s | -0.0182s | improved |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1318s | -0.0163s | improved |
| `ngap_rel18.6_specs` | 0.0689s | 0.0783s | -0.0094s | improved |
| `lteNRRCC` | 0.1083s | 0.1050s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.50 MB | 4.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.12 MB | 7.23 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.45 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.78 MB | 6.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0411s | -0.0037s | improved |
| `f1ap_rel18.6_specs` | 0.0940s | 0.1140s | -0.0200s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0805s | -0.0159s | improved |
| `lteNRRCC` | 0.1005s | 0.1394s | -0.0389s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.33 MB | 8.49 MB | 0.0% | 115.5% |
| `f1ap_rel18.6_specs` | 8.79 MB | 8.78 MB | 146.5% | 148.4% |
| `ngap_rel18.6_specs` | 9.12 MB | 8.48 MB | 134.8% | 105.8% |
| `lteNRRCC` | 8.53 MB | 70.53 MB | 120.9% | 146.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0310s | 0.0387s | -0.0077s | improved |
| `f1ap_rel18.6_specs` | 0.0920s | 0.1079s | -0.0159s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0746s | -0.0106s | improved |
| `lteNRRCC` | 0.0941s | 0.1255s | -0.0314s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 30.39 MB | 0.0% | 78.5% |
| `f1ap_rel18.6_specs` | 20.31 MB | 164.19 MB | 134.9% | 83.1% |
| `ngap_rel18.6_specs` | 24.20 MB | 24.07 MB | 0.0% | 135.6% |
| `lteNRRCC` | 17.14 MB | 29.04 MB | 144.3% | 113.0% |
<!-- BENCH_RESULTS_END -->
