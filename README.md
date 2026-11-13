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
Generated: 2026-11-13T02:30:12.681964+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0402s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1257s | 0.1237s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0863s | 0.0854s | +0.0009s | worse |
| `lteNRRCC` | 0.1304s | 0.1288s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 76.9% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.6% |
| `lteNRRCC` | 72.40 MB | 100.18 MB | 103.2% | 103.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0292s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.1095s | 0.0976s | +0.0119s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0661s | +0.0096s | worse |
| `lteNRRCC` | 0.1190s | 0.1007s | +0.0183s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.18 MB | 34.65 MB | 70.3% | 106.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.9% | 102.8% |
| `ngap_rel18.6_specs` | 18.09 MB | 72.65 MB | 110.3% | 105.6% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 104.8% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0441s | 0.0611s | -0.0170s | improved |
| `f1ap_rel18.6_specs` | 0.1328s | 0.1773s | -0.0445s | improved |
| `ngap_rel18.6_specs` | 0.0928s | 0.1245s | -0.0317s | improved |
| `lteNRRCC` | 0.1380s | 0.1694s | -0.0314s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 53.73 MB | 73.9% | 103.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 103.4% | 101.3% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 104.5% | 103.7% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 101.6% | 101.3% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0276s | 0.0402s | -0.0126s | improved |
| `f1ap_rel18.6_specs` | 0.0784s | 0.1168s | -0.0384s | improved |
| `ngap_rel18.6_specs` | 0.0536s | 0.0810s | -0.0274s | improved |
| `lteNRRCC` | 0.0884s | 0.1400s | -0.0516s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.70 MB | 0.0% | 149.6% |
| `f1ap_rel18.6_specs` | 9.12 MB | 9.13 MB | 149.7% | 152.3% |
| `ngap_rel18.6_specs` | 8.50 MB | 8.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 9.06 MB | 68.35 MB | 145.8% | 145.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0466s | 0.0419s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1303s | 0.1192s | +0.0111s | worse |
| `ngap_rel18.6_specs` | 0.0945s | 0.0822s | +0.0123s | worse |
| `lteNRRCC` | 0.1347s | 0.1368s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 10.29 MB | 0.0% | 80.9% |
| `f1ap_rel18.6_specs` | 10.66 MB | 124.03 MB | 222.3% | 160.1% |
| `ngap_rel18.6_specs` | 10.33 MB | 10.83 MB | 154.1% | 229.8% |
| `lteNRRCC` | 9.38 MB | 74.28 MB | 209.5% | 157.3% |
<!-- BENCH_RESULTS_END -->
