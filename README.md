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
Generated: 2026-11-08T16:34:46.921751+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0391s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1265s | 0.1221s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0863s | 0.0845s | +0.0018s | worse |
| `lteNRRCC` | 0.1288s | 0.1261s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 16.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.7% |
| `lteNRRCC` | 72.38 MB | 100.11 MB | 103.3% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0468s | 0.0360s | +0.0108s | worse |
| `f1ap_rel18.6_specs` | 0.1422s | 0.1106s | +0.0316s | worse |
| `ngap_rel18.6_specs` | 0.0988s | 0.0751s | +0.0237s | worse |
| `lteNRRCC` | 0.1556s | 0.1195s | +0.0361s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 34.65 MB | 79.3% | 102.9% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 102.8% | 102.5% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 107.1% | 103.4% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.7% | 102.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0497s | 0.0358s | +0.0139s | worse |
| `f1ap_rel18.6_specs` | 0.1514s | 0.1174s | +0.0340s | worse |
| `ngap_rel18.6_specs` | 0.1054s | 0.0822s | +0.0232s | worse |
| `lteNRRCC` | 0.1476s | 0.1120s | +0.0356s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.85 MB | 53.73 MB | 59.4% | 102.9% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 103.2% | 101.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 104.2% | 101.6% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 101.5% | 101.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0390s | -0.0047s | improved |
| `f1ap_rel18.6_specs` | 0.0968s | 0.1108s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0699s | 0.0761s | -0.0062s | improved |
| `lteNRRCC` | 0.1140s | 0.1387s | -0.0247s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 8.12 MB | 0.0% | 115.2% |
| `f1ap_rel18.6_specs` | 8.62 MB | 8.68 MB | 103.4% | 202.3% |
| `ngap_rel18.6_specs` | 8.20 MB | 8.43 MB | 204.6% | 98.4% |
| `lteNRRCC` | 51.84 MB | 60.80 MB | 100.7% | 110.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0389s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1100s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0755s | 0.0815s | -0.0060s | improved |
| `lteNRRCC` | 0.1268s | 0.1250s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.09 MB | 0.0% | 213.4% |
| `f1ap_rel18.6_specs` | 9.62 MB | 11.64 MB | 82.1% | 224.4% |
| `ngap_rel18.6_specs` | 8.96 MB | 9.21 MB | 159.9% | 158.5% |
| `lteNRRCC` | 9.36 MB | 84.44 MB | 104.0% | 223.7% |
<!-- BENCH_RESULTS_END -->
