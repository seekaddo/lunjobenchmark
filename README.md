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
Generated: 2026-11-11T01:48:15.278850+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0424s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1282s | 0.1293s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0882s | 0.0882s | +0.0000s | flat |
| `lteNRRCC` | 0.1294s | 0.1286s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 91.3% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 105.5% |
| `lteNRRCC` | 72.38 MB | 100.11 MB | 103.2% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0361s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1131s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0773s | -0.0023s | improved |
| `lteNRRCC` | 0.1191s | 0.1199s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 34.65 MB | 86.4% | 103.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 107.4% | 101.6% |
| `ngap_rel18.6_specs` | 18.04 MB | 72.65 MB | 109.5% | 102.2% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 101.8% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0472s | 0.0490s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1468s | 0.1477s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.1025s | 0.1007s | +0.0018s | worse |
| `lteNRRCC` | 0.1439s | 0.1426s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.81 MB | 53.73 MB | 85.7% | 106.2% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 106.7% | 101.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 108.7% | 103.4% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 103.1% | 101.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0413s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0950s | 0.1108s | -0.0158s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0770s | -0.0108s | improved |
| `lteNRRCC` | 0.1129s | 0.1401s | -0.0272s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.24 MB | 0.0% | 98.8% |
| `f1ap_rel18.6_specs` | 8.99 MB | 106.64 MB | 98.3% | 128.3% |
| `ngap_rel18.6_specs` | 8.37 MB | 8.50 MB | 99.4% | 94.5% |
| `lteNRRCC` | 8.61 MB | 68.41 MB | 99.9% | 108.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0308s | +0.0102s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.0895s | +0.0232s | worse |
| `ngap_rel18.6_specs` | 0.0804s | 0.0635s | +0.0169s | worse |
| `lteNRRCC` | 0.1309s | 0.0986s | +0.0323s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.55 MB | 0.0% | 74.2% |
| `f1ap_rel18.6_specs` | 10.07 MB | 10.25 MB | 150.3% | 148.3% |
| `ngap_rel18.6_specs` | 10.70 MB | 9.35 MB | 94.8% | 147.5% |
| `lteNRRCC` | 9.62 MB | 90.90 MB | 93.6% | 146.3% |
<!-- BENCH_RESULTS_END -->
