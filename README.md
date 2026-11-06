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
Generated: 2026-11-06T02:08:34.455821+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0396s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1272s | 0.1256s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0880s | 0.0872s | +0.0008s | worse |
| `lteNRRCC` | 0.1320s | 0.1296s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 87.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 101.9% |
| `lteNRRCC` | 72.35 MB | 100.18 MB | 101.6% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0454s | 0.0387s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.1393s | 0.1169s | +0.0224s | worse |
| `ngap_rel18.6_specs` | 0.0958s | 0.0824s | +0.0134s | worse |
| `lteNRRCC` | 0.1548s | 0.1320s | +0.0228s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 34.65 MB | 19.8% | 106.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.7% | 101.2% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 103.6% | 101.7% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 102.7% | 101.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0391s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1217s | 0.1200s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0919s | 0.0816s | +0.0103s | worse |
| `lteNRRCC` | 0.1117s | 0.1040s | +0.0077s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 53.73 MB | 57.1% | 103.6% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 108.0% | 101.5% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 105.0% | 102.0% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 102.0% | 101.5% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0342s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.0940s | +0.0158s | worse |
| `ngap_rel18.6_specs` | 0.0744s | 0.0661s | +0.0083s | worse |
| `lteNRRCC` | 0.1392s | 0.1189s | +0.0203s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.50 MB | 0.0% | 162.7% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.11 MB | 160.2% | 160.7% |
| `ngap_rel18.6_specs` | 7.99 MB | 8.18 MB | 105.0% | 228.7% |
| `lteNRRCC` | 51.75 MB | 52.77 MB | 109.8% | 224.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0345s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.1159s | 0.1065s | +0.0094s | worse |
| `ngap_rel18.6_specs` | 0.0805s | 0.0743s | +0.0062s | worse |
| `lteNRRCC` | 0.1161s | 0.1149s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.15 MB | 0.0% | 129.9% |
| `f1ap_rel18.6_specs` | 10.17 MB | 140.24 MB | 129.8% | 129.7% |
| `ngap_rel18.6_specs` | 10.02 MB | 10.16 MB | 128.6% | 129.8% |
| `lteNRRCC` | 73.77 MB | 90.52 MB | 129.6% | 131.0% |
<!-- BENCH_RESULTS_END -->
