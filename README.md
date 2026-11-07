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
Generated: 2026-11-07T16:13:49.978622+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0425s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1222s | 0.1261s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0836s | 0.0872s | -0.0036s | improved |
| `lteNRRCC` | 0.1267s | 0.1327s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 87.0% | 103.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.8% |
| `lteNRRCC` | 72.38 MB | 100.18 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0302s | 0.0472s | -0.0170s | improved |
| `f1ap_rel18.6_specs` | 0.0975s | 0.1391s | -0.0416s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0975s | -0.0324s | improved |
| `lteNRRCC` | 0.0936s | 0.1550s | -0.0614s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 34.65 MB | 78.9% | 104.3% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 104.5% | 101.8% |
| `ngap_rel18.6_specs` | 18.06 MB | 72.65 MB | 111.1% | 100.0% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.3% | 103.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0552s | 0.0533s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1646s | 0.1635s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.1153s | 0.1136s | +0.0017s | worse |
| `lteNRRCC` | 0.1617s | 0.1597s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.67 MB | 53.73 MB | 75.9% | 105.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 102.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.1% | 101.4% |
| `lteNRRCC` | 72.61 MB | 100.36 MB | 101.4% | 101.1% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0341s | +0.0050s | worse |
| `f1ap_rel18.6_specs` | 0.1057s | 0.0908s | +0.0149s | worse |
| `ngap_rel18.6_specs` | 0.0735s | 0.0628s | +0.0107s | worse |
| `lteNRRCC` | 0.1369s | 0.1146s | +0.0223s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 6.83 MB | 0.0% | 101.9% |
| `f1ap_rel18.6_specs` | 7.98 MB | 8.05 MB | 170.0% | 164.7% |
| `ngap_rel18.6_specs` | 7.68 MB | 7.69 MB | 152.9% | 167.9% |
| `lteNRRCC` | 51.71 MB | 51.41 MB | 226.8% | 227.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0381s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1066s | 0.1118s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0794s | -0.0036s | improved |
| `lteNRRCC` | 0.1250s | 0.1288s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 8.59 MB | 0.0% | 80.8% |
| `f1ap_rel18.6_specs` | 9.57 MB | 164.20 MB | 159.3% | 106.3% |
| `ngap_rel18.6_specs` | 8.90 MB | 8.96 MB | 153.6% | 166.2% |
| `lteNRRCC` | 8.75 MB | 73.47 MB | 153.6% | 154.8% |
<!-- BENCH_RESULTS_END -->
