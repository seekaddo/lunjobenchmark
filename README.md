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
Generated: 2026-10-30T16:51:38.881090+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0395s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1269s | 0.1209s | +0.0060s | worse |
| `ngap_rel18.6_specs` | 0.0860s | 0.0817s | +0.0043s | worse |
| `lteNRRCC` | 0.1291s | 0.1266s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.92 MB | 53.55 MB | 25.0% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 103.6% |
| `lteNRRCC` | 72.40 MB | 100.18 MB | 103.2% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0475s | 0.0455s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1440s | 0.1379s | +0.0061s | worse |
| `ngap_rel18.6_specs` | 0.1005s | 0.0966s | +0.0039s | worse |
| `lteNRRCC` | 0.1583s | 0.1546s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 34.65 MB | 82.1% | 105.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.6% | 101.2% |
| `ngap_rel18.6_specs` | 17.93 MB | 72.65 MB | 106.9% | 103.2% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.7% | 103.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0534s | 0.0602s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.1650s | 0.1848s | -0.0198s | improved |
| `ngap_rel18.6_specs` | 0.1156s | 0.1277s | -0.0121s | improved |
| `lteNRRCC` | 0.1607s | 0.1819s | -0.0212s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 53.73 MB | 78.6% | 105.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 101.1% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 103.7% | 102.9% |
| `lteNRRCC` | 72.58 MB | 100.36 MB | 101.4% | 102.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0325s | +0.0081s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.0914s | +0.0196s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0674s | +0.0114s | worse |
| `lteNRRCC` | 0.1405s | 0.1119s | +0.0286s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.32 MB | 8.38 MB | 0.0% | 222.1% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.68 MB | 90.3% | 0.0% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.25 MB | 75.4% | 95.7% |
| `lteNRRCC` | 8.61 MB | 57.65 MB | 96.7% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0439s | 0.0401s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.1286s | 0.1125s | +0.0161s | worse |
| `ngap_rel18.6_specs` | 0.0886s | 0.0798s | +0.0088s | worse |
| `lteNRRCC` | 0.1340s | 0.1300s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.60 MB | 10.22 MB | 0.0% | 116.4% |
| `f1ap_rel18.6_specs` | 10.51 MB | 10.37 MB | 93.1% | 117.5% |
| `ngap_rel18.6_specs` | 10.51 MB | 9.75 MB | 236.5% | 118.1% |
| `lteNRRCC` | 9.12 MB | 99.34 MB | 161.5% | 118.5% |
<!-- BENCH_RESULTS_END -->
