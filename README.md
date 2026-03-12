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
- `bench_results/`: latest and historical benchmark output

## Assumptions

- The benchmark repo has access to release archives named like `voltcc-v<version>-<target>.tar.gz`.
- `preparebin.sh` prefers `./releases/` and falls back to `../releases/` for local nested-repo development.
- The copied upstream benchmark scripts execute the prepared binary from `./zig-out/bin/voltcc`, matching the local `test_semantic` script layout.

## Latest Results

<!-- BENCH_RESULTS_START -->
Generated: 2026-03-12T18:18:59.526641+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0999s | 0.0984s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.3095s | 0.3055s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.2253s | 0.2270s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.30 MB | 5.37 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.30 MB | 453.07 MB | 0.0% | 95.8% |
| `ngap_rel18.6_specs` | 5.81 MB | 234.14 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0688s | 0.0702s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1961s | 0.1944s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.1425s | 0.1425s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.73 MB | 4.67 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.36 MB | 220.88 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 5.15 MB | 248.10 MB | 0.0% | 91.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0722s | 0.0708s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.2007s | 0.1919s | +0.0088s | worse |
| `ngap_rel18.6_specs` | 0.1474s | 0.1411s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.91 MB | 6.64 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.46 MB | 339.91 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 7.18 MB | 372.60 MB | 0.0% | 92.3% |
<!-- BENCH_RESULTS_END -->
