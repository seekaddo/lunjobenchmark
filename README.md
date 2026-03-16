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
Generated: 2026-03-16T16:11:09.492045+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0418s | 0.0384s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.1304s | 0.1202s | +0.0102s | worse |
| `ngap_rel18.6_specs` | 0.0903s | 0.0868s | +0.0035s | worse |
| `lteNRRCC` | 0.1267s | 0.1259s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.53 MB | 55.78 MB | 110.5% | 106.2% |
| `f1ap_rel18.6_specs` | 32.53 MB | 176.91 MB | 110.0% | 104.1% |
| `ngap_rel18.6_specs` | 22.41 MB | 125.78 MB | 112.5% | 103.6% |
| `lteNRRCC` | 72.33 MB | 100.09 MB | 105.1% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0347s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0970s | 0.1033s | -0.0063s | improved |
| `ngap_rel18.6_specs` | 0.0683s | 0.0703s | -0.0020s | improved |
| `lteNRRCC` | 0.1301s | 0.1213s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.59 MB | 37.88 MB | 92.6% | 110.0% |
| `f1ap_rel18.6_specs` | 22.38 MB | 111.84 MB | 108.8% | 105.0% |
| `ngap_rel18.6_specs` | 16.41 MB | 80.06 MB | 110.7% | 106.5% |
| `lteNRRCC` | 48.64 MB | 66.33 MB | 104.5% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0351s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0939s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.0663s | -0.0007s | improved |
| `lteNRRCC` | 0.1146s | 0.1155s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 57.88 MB | 16.3% | 110.0% |
| `f1ap_rel18.6_specs` | 34.53 MB | 178.98 MB | 109.7% | 105.1% |
| `ngap_rel18.6_specs` | 24.43 MB | 127.80 MB | 111.5% | 108.9% |
| `lteNRRCC` | 74.51 MB | 102.52 MB | 106.8% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0287s | 0.0206s | +0.0081s | worse |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0623s | +0.0311s | worse |
| `ngap_rel18.6_specs` | 0.0701s | 0.0425s | +0.0276s | worse |
| `lteNRRCC` | 0.1001s | 0.0705s | +0.0296s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.11 MB | 5.06 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 11.36 MB | 10.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 10.84 MB | 8.28 MB | 2.2% | 0.0% |
| `lteNRRCC` | 7.14 MB | 6.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0402s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.1108s | +0.0059s | worse |
| `ngap_rel18.6_specs` | 0.0810s | 0.0784s | +0.0026s | worse |
| `lteNRRCC` | 0.1415s | 0.1427s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.84 MB | 7.73 MB | 155.4% | 76.0% |
| `f1ap_rel18.6_specs` | 8.12 MB | 115.11 MB | 158.1% | 111.9% |
| `ngap_rel18.6_specs` | 8.06 MB | 7.97 MB | 89.5% | 76.8% |
| `lteNRRCC` | 51.49 MB | 51.12 MB | 204.1% | 109.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0406s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1106s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0763s | +0.0026s | worse |
| `lteNRRCC` | 0.1246s | 0.1258s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.99 MB | 10.50 MB | 164.2% | 218.8% |
| `f1ap_rel18.6_specs` | 10.13 MB | 164.96 MB | 105.4% | 106.4% |
| `ngap_rel18.6_specs` | 9.21 MB | 10.79 MB | 100.0% | 117.3% |
| `lteNRRCC` | 9.37 MB | 99.55 MB | 110.3% | 229.1% |
<!-- BENCH_RESULTS_END -->
