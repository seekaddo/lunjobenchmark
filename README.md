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
Generated: 2026-10-21T15:00:32.682984+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0361s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1188s | 0.1134s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0789s | +0.0030s | worse |
| `lteNRRCC` | 0.1265s | 0.1214s | +0.0051s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.98 MB | 53.55 MB | 79.2% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0216s | +0.0180s | worse |
| `f1ap_rel18.6_specs` | 0.1238s | 0.0603s | +0.0635s | worse |
| `ngap_rel18.6_specs` | 0.0820s | 0.0403s | +0.0417s | worse |
| `lteNRRCC` | 0.1288s | 0.0741s | +0.0547s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.75 MB | 34.65 MB | 78.3% | 103.6% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 106.9% | 101.4% |
| `ngap_rel18.6_specs` | 18.15 MB | 72.65 MB | 104.2% | 102.0% |
| `lteNRRCC` | 46.66 MB | 64.21 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0565s | 0.0552s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1686s | 0.1660s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.1213s | 0.1149s | +0.0064s | worse |
| `lteNRRCC` | 0.1643s | 0.1654s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 53.73 MB | 68.8% | 105.3% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 108.6% | 101.0% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.1% | 101.4% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 102.7% | 101.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0154s | +0.0207s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.0982s | +0.0124s | worse |
| `ngap_rel18.6_specs` | 0.0537s | 0.0559s | -0.0022s | improved |
| `lteNRRCC` | 0.0868s | 0.0951s | -0.0083s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.27 MB | 7.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.94 MB | 9.03 MB | 0.0% | 1.8% |
| `ngap_rel18.6_specs` | 7.89 MB | 9.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.06 MB | 3.94 MB | 0.0% | 0.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0466s | -0.0079s | improved |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1382s | -0.0247s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0983s | -0.0205s | improved |
| `lteNRRCC` | 0.1251s | 0.1405s | -0.0154s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.77 MB | 0.0% | 79.0% |
| `f1ap_rel18.6_specs` | 9.85 MB | 10.34 MB | 157.0% | 101.8% |
| `ngap_rel18.6_specs` | 8.87 MB | 9.12 MB | 159.7% | 159.4% |
| `lteNRRCC` | 8.54 MB | 90.62 MB | 155.6% | 110.2% |
<!-- BENCH_RESULTS_END -->
