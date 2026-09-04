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
Generated: 2026-09-04T23:52:08.036164+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0346s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1078s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0729s | +0.0029s | worse |
| `lteNRRCC` | 0.1197s | 0.1161s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 65.5% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0353s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0944s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0684s | 0.0667s | +0.0017s | worse |
| `lteNRRCC` | 0.1290s | 0.1292s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 36.10 MB | 80.8% | 103.8% |
| `f1ap_rel18.6_specs` | 22.21 MB | 103.26 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.13 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.57 MB | 66.51 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0342s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0895s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0632s | 0.0637s | -0.0005s | improved |
| `lteNRRCC` | 0.1166s | 0.1168s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 55.82 MB | 76.0% | 103.7% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.28 MB | 103.4% | 101.9% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.60 MB | 104.2% | 104.9% |
| `lteNRRCC` | 74.19 MB | 102.55 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0280s | 0.0261s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1102s | 0.0817s | +0.0285s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0485s | +0.0269s | worse |
| `lteNRRCC` | 0.1116s | 0.0944s | +0.0172s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.78 MB | 4.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.47 MB | 9.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.81 MB | 7.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.20 MB | 5.89 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0458s | 0.0377s | +0.0081s | worse |
| `f1ap_rel18.6_specs` | 0.1268s | 0.1017s | +0.0251s | worse |
| `ngap_rel18.6_specs` | 0.0875s | 0.0724s | +0.0151s | worse |
| `lteNRRCC` | 0.1468s | 0.1124s | +0.0344s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.75 MB | 8.45 MB | 97.7% | 151.6% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.61 MB | 151.3% | 142.8% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.49 MB | 156.3% | 93.0% |
| `lteNRRCC` | 8.66 MB | 8.07 MB | 151.7% | 151.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0379s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1090s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0776s | -0.0002s | improved |
| `lteNRRCC` | 0.1275s | 0.1248s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.47 MB | 8.67 MB | 166.1% | 160.2% |
| `f1ap_rel18.6_specs` | 9.63 MB | 164.20 MB | 158.2% | 160.0% |
| `ngap_rel18.6_specs` | 10.64 MB | 8.90 MB | 233.3% | 160.1% |
| `lteNRRCC` | 8.44 MB | 98.14 MB | 79.1% | 105.3% |
<!-- BENCH_RESULTS_END -->
