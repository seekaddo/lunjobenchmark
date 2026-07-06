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
Generated: 2026-07-06T23:13:46.505647+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0330s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1195s | 0.1073s | +0.0122s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0724s | +0.0044s | worse |
| `lteNRRCC` | 0.1206s | 0.1171s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 22.2% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0355s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0953s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0720s | 0.0708s | +0.0012s | worse |
| `lteNRRCC` | 0.1292s | 0.1286s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 36.02 MB | 81.5% | 111.1% |
| `f1ap_rel18.6_specs` | 22.20 MB | 103.40 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.22 MB | 111.5% | 104.4% |
| `lteNRRCC` | 48.30 MB | 65.98 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0346s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0963s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0675s | -0.0029s | improved |
| `lteNRRCC` | 0.1257s | 0.1157s | +0.0100s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 54.99 MB | 82.1% | 110.3% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.59 MB | 106.2% | 105.3% |
| `ngap_rel18.6_specs` | 24.61 MB | 116.98 MB | 111.5% | 107.0% |
| `lteNRRCC` | 74.29 MB | 102.73 MB | 103.1% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0291s | -0.0085s | improved |
| `f1ap_rel18.6_specs` | 0.0704s | 0.0816s | -0.0112s | improved |
| `ngap_rel18.6_specs` | 0.0485s | 0.0479s | +0.0006s | worse |
| `lteNRRCC` | 0.0774s | 0.0772s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.17 MB | 3.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.53 MB | 7.67 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.77 MB | 8.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.75 MB | 7.48 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0409s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1155s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0817s | -0.0047s | improved |
| `lteNRRCC` | 0.1414s | 0.1411s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 8.11 MB | 104.7% | 96.6% |
| `f1ap_rel18.6_specs` | 8.43 MB | 106.63 MB | 155.7% | 152.7% |
| `ngap_rel18.6_specs` | 8.11 MB | 7.98 MB | 164.7% | 87.2% |
| `lteNRRCC` | 51.33 MB | 70.55 MB | 106.9% | 153.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0393s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1206s | 0.1157s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0839s | 0.0788s | +0.0051s | worse |
| `lteNRRCC` | 0.1389s | 0.1269s | +0.0120s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 9.77 MB | 162.8% | 105.0% |
| `f1ap_rel18.6_specs` | 10.56 MB | 164.19 MB | 223.2% | 109.5% |
| `ngap_rel18.6_specs` | 9.14 MB | 10.68 MB | 164.3% | 215.7% |
| `lteNRRCC` | 8.74 MB | 101.70 MB | 85.1% | 157.3% |
<!-- BENCH_RESULTS_END -->
