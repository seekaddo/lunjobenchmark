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
Generated: 2026-11-14T02:10:16.708006+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0420s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1250s | 0.1290s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0859s | 0.0898s | -0.0039s | improved |
| `lteNRRCC` | 0.1296s | 0.1323s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 78.0% | 107.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.8% | 104.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.3% | 103.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0464s | 0.0388s | +0.0076s | worse |
| `f1ap_rel18.6_specs` | 0.1389s | 0.1207s | +0.0182s | worse |
| `ngap_rel18.6_specs` | 0.0958s | 0.0851s | +0.0107s | worse |
| `lteNRRCC` | 0.1529s | 0.1323s | +0.0206s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.93 MB | 34.65 MB | 88.9% | 107.3% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 104.5% | 104.6% |
| `ngap_rel18.6_specs` | 17.93 MB | 72.65 MB | 105.6% | 104.5% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 103.7% | 104.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0439s | 0.0312s | +0.0127s | worse |
| `f1ap_rel18.6_specs` | 0.1364s | 0.1046s | +0.0318s | worse |
| `ngap_rel18.6_specs` | 0.0944s | 0.0705s | +0.0239s | worse |
| `lteNRRCC` | 0.1380s | 0.1014s | +0.0366s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.00 MB | 53.73 MB | 86.7% | 105.3% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.6% | 102.4% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 106.7% | 103.2% |
| `lteNRRCC` | 72.61 MB | 100.36 MB | 102.9% | 102.4% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0397s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0951s | 0.1129s | -0.0178s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0769s | -0.0118s | improved |
| `lteNRRCC` | 0.1135s | 0.1374s | -0.0239s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.64 MB | 0.0% | 106.5% |
| `f1ap_rel18.6_specs` | 8.74 MB | 8.99 MB | 109.1% | 99.3% |
| `ngap_rel18.6_specs` | 8.37 MB | 8.47 MB | 134.0% | 122.9% |
| `lteNRRCC` | 8.61 MB | 68.80 MB | 193.0% | 192.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0336s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.1125s | 0.0990s | +0.0135s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0661s | +0.0116s | worse |
| `lteNRRCC` | 0.1271s | 0.1088s | +0.0183s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.53 MB | 0.0% | 81.3% |
| `f1ap_rel18.6_specs` | 9.64 MB | 164.17 MB | 160.1% | 107.2% |
| `ngap_rel18.6_specs` | 10.82 MB | 8.96 MB | 234.1% | 80.7% |
| `lteNRRCC` | 8.69 MB | 80.84 MB | 178.4% | 108.0% |
<!-- BENCH_RESULTS_END -->
