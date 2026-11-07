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
Generated: 2026-11-07T01:45:32.082250+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0425s | 0.0440s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1261s | 0.1326s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0872s | 0.0919s | -0.0047s | improved |
| `lteNRRCC` | 0.1327s | 0.1335s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 80.8% | 106.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.1% | 102.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.4% |
| `lteNRRCC` | 72.40 MB | 100.18 MB | 103.2% | 102.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0472s | 0.0383s | +0.0089s | worse |
| `f1ap_rel18.6_specs` | 0.1391s | 0.1148s | +0.0243s | worse |
| `ngap_rel18.6_specs` | 0.0975s | 0.0792s | +0.0183s | worse |
| `lteNRRCC` | 0.1550s | 0.1225s | +0.0325s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 34.65 MB | 78.6% | 106.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.7% | 102.5% |
| `ngap_rel18.6_specs` | 17.92 MB | 72.65 MB | 107.1% | 103.4% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.7% | 101.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0533s | 0.0396s | +0.0137s | worse |
| `f1ap_rel18.6_specs` | 0.1635s | 0.1204s | +0.0431s | worse |
| `ngap_rel18.6_specs` | 0.1136s | 0.0849s | +0.0287s | worse |
| `lteNRRCC` | 0.1597s | 0.1136s | +0.0461s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 23.4% | 105.6% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 102.9% | 102.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.4% | 101.5% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 101.4% | 102.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0324s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0914s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0628s | 0.0644s | -0.0016s | improved |
| `lteNRRCC` | 0.1146s | 0.1121s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.83 MB | 0.0% | 107.2% |
| `f1ap_rel18.6_specs` | 8.56 MB | 105.14 MB | 50.1% | 110.0% |
| `ngap_rel18.6_specs` | 8.51 MB | 8.38 MB | 132.6% | 133.3% |
| `lteNRRCC` | 7.38 MB | 8.50 MB | 244.3% | 101.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0362s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1011s | +0.0107s | worse |
| `ngap_rel18.6_specs` | 0.0794s | 0.0722s | +0.0072s | worse |
| `lteNRRCC` | 0.1288s | 0.1123s | +0.0165s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 8.59 MB | 0.0% | 161.1% |
| `f1ap_rel18.6_specs` | 9.41 MB | 164.20 MB | 161.6% | 161.3% |
| `ngap_rel18.6_specs` | 8.78 MB | 8.96 MB | 160.4% | 159.6% |
| `lteNRRCC` | 8.44 MB | 101.70 MB | 79.1% | 157.3% |
<!-- BENCH_RESULTS_END -->
