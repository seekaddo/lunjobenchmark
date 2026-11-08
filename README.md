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
Generated: 2026-11-08T01:13:51.277863+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0394s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1221s | 0.1222s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0845s | 0.0836s | +0.0009s | worse |
| `lteNRRCC` | 0.1261s | 0.1267s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 87.0% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.8% |
| `lteNRRCC` | 72.37 MB | 100.11 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0302s | +0.0058s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.0975s | +0.0131s | worse |
| `ngap_rel18.6_specs` | 0.0751s | 0.0651s | +0.0100s | worse |
| `lteNRRCC` | 0.1195s | 0.0936s | +0.0259s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.85 MB | 34.65 MB | 81.8% | 107.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 18.06 MB | 72.65 MB | 104.5% | 104.3% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0552s | -0.0194s | improved |
| `f1ap_rel18.6_specs` | 0.1174s | 0.1646s | -0.0472s | improved |
| `ngap_rel18.6_specs` | 0.0822s | 0.1153s | -0.0331s | improved |
| `lteNRRCC` | 0.1120s | 0.1617s | -0.0497s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 53.73 MB | 89.5% | 107.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 104.0% | 101.5% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 110.5% | 101.9% |
| `lteNRRCC` | 72.64 MB | 100.36 MB | 101.8% | 101.4% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0391s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1057s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0735s | +0.0026s | worse |
| `lteNRRCC` | 0.1387s | 0.1369s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 7.82 MB | 0.0% | 163.0% |
| `f1ap_rel18.6_specs` | 8.47 MB | 8.56 MB | 168.2% | 190.0% |
| `ngap_rel18.6_specs` | 8.15 MB | 8.06 MB | 165.9% | 83.1% |
| `lteNRRCC` | 51.84 MB | 58.08 MB | 103.3% | 109.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0380s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1066s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0815s | 0.0758s | +0.0057s | worse |
| `lteNRRCC` | 0.1250s | 0.1250s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.95 MB | 0.0% | 94.9% |
| `f1ap_rel18.6_specs` | 9.70 MB | 164.20 MB | 183.4% | 158.4% |
| `ngap_rel18.6_specs` | 8.96 MB | 8.97 MB | 155.9% | 79.9% |
| `lteNRRCC` | 8.63 MB | 84.77 MB | 97.3% | 156.3% |
<!-- BENCH_RESULTS_END -->
