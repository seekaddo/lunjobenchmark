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
Generated: 2026-10-31T15:41:22.814454+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0395s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1170s | 0.1227s | -0.0057s | improved |
| `ngap_rel18.6_specs` | 0.0822s | 0.0839s | -0.0017s | improved |
| `lteNRRCC` | 0.1228s | 0.1283s | -0.0055s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 86.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0308s | 0.0370s | -0.0062s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.1149s | -0.0219s | improved |
| `ngap_rel18.6_specs` | 0.0735s | 0.0804s | -0.0069s | improved |
| `lteNRRCC` | 0.1027s | 0.1253s | -0.0226s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.84 MB | 34.65 MB | 75.0% | 104.3% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 104.3% | 101.8% |
| `ngap_rel18.6_specs` | 18.04 MB | 72.65 MB | 105.6% | 105.0% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 104.7% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0532s | 0.0419s | +0.0113s | worse |
| `f1ap_rel18.6_specs` | 0.1653s | 0.1307s | +0.0346s | worse |
| `ngap_rel18.6_specs` | 0.1194s | 0.0908s | +0.0286s | worse |
| `lteNRRCC` | 0.1631s | 0.1344s | +0.0287s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 53.73 MB | 78.6% | 105.3% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 102.8% | 102.1% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.1% | 101.4% |
| `lteNRRCC` | 72.62 MB | 100.36 MB | 101.3% | 101.1% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0390s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1096s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0780s | 0.0758s | +0.0022s | worse |
| `lteNRRCC` | 0.1279s | 0.1386s | -0.0107s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 8.43 MB | 0.0% | 111.9% |
| `f1ap_rel18.6_specs` | 8.87 MB | 100.88 MB | 112.8% | 222.2% |
| `ngap_rel18.6_specs` | 8.82 MB | 8.50 MB | 112.3% | 111.6% |
| `lteNRRCC` | 8.68 MB | 68.61 MB | 107.9% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0405s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1049s | 0.1156s | -0.0107s | improved |
| `ngap_rel18.6_specs` | 0.0724s | 0.0809s | -0.0085s | improved |
| `lteNRRCC` | 0.1167s | 0.1289s | -0.0122s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 10.21 MB | 130.2% | 200.1% |
| `f1ap_rel18.6_specs` | 11.40 MB | 154.02 MB | 120.3% | 104.9% |
| `ngap_rel18.6_specs` | 9.94 MB | 10.95 MB | 108.7% | 114.9% |
| `lteNRRCC` | 9.25 MB | 98.27 MB | 93.8% | 107.4% |
<!-- BENCH_RESULTS_END -->
