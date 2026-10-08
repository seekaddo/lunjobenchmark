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
Generated: 2026-10-08T01:42:38.391721+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0376s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1152s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0794s | -0.0030s | improved |
| `lteNRRCC` | 0.1209s | 0.1242s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 16.4% | 100.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0246s | +0.0082s | worse |
| `f1ap_rel18.6_specs` | 0.0954s | 0.0593s | +0.0361s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0445s | +0.0220s | worse |
| `lteNRRCC` | 0.1181s | 0.0766s | +0.0415s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 36.35 MB | 81.0% | 104.2% |
| `f1ap_rel18.6_specs` | 22.20 MB | 103.40 MB | 100.0% | 101.8% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.32 MB | 104.8% | 102.4% |
| `lteNRRCC` | 48.45 MB | 66.46 MB | 100.0% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0344s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0940s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0647s | 0.0644s | +0.0003s | worse |
| `lteNRRCC` | 0.1185s | 0.1204s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.90 MB | 52.8% | 107.7% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.62 MB | 103.6% | 101.8% |
| `ngap_rel18.6_specs` | 24.36 MB | 117.62 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.85 MB | 102.84 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0587s | -0.0171s | improved |
| `f1ap_rel18.6_specs` | 0.0762s | 0.0793s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0572s | 0.0497s | +0.0075s | worse |
| `lteNRRCC` | 0.0979s | 0.0931s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.45 MB | 192 KB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.09 MB | 10.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 4.81 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.27 MB | 4.33 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0404s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.0962s | 0.1107s | -0.0145s | improved |
| `ngap_rel18.6_specs` | 0.0679s | 0.0757s | -0.0078s | improved |
| `lteNRRCC` | 0.1101s | 0.1298s | -0.0197s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.09 MB | 8.35 MB | 0.0% | 131.6% |
| `f1ap_rel18.6_specs` | 8.39 MB | 106.67 MB | 130.7% | 125.9% |
| `ngap_rel18.6_specs` | 8.34 MB | 8.54 MB | 244.4% | 124.0% |
| `lteNRRCC` | 8.05 MB | 68.58 MB | 259.4% | 201.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0352s | +0.0043s | worse |
| `f1ap_rel18.6_specs` | 0.1111s | 0.0987s | +0.0124s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0676s | +0.0085s | worse |
| `lteNRRCC` | 0.1287s | 0.1113s | +0.0174s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.76 MB | 0.0% | 153.5% |
| `f1ap_rel18.6_specs` | 10.04 MB | 164.17 MB | 174.1% | 150.9% |
| `ngap_rel18.6_specs` | 8.94 MB | 10.77 MB | 155.3% | 106.5% |
| `lteNRRCC` | 9.22 MB | 98.12 MB | 99.5% | 154.3% |
<!-- BENCH_RESULTS_END -->
