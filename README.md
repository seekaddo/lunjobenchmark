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
Generated: 2026-08-17T10:37:50.023275+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0351s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1101s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0804s | 0.0753s | +0.0051s | worse |
| `lteNRRCC` | 0.1219s | 0.1193s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 76.0% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0258s | 0.0219s | +0.0039s | worse |
| `f1ap_rel18.6_specs` | 0.0780s | 0.0692s | +0.0088s | worse |
| `ngap_rel18.6_specs` | 0.0525s | 0.0458s | +0.0067s | worse |
| `lteNRRCC` | 0.0944s | 0.0826s | +0.0118s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.36 MB | 36.18 MB | 77.3% | 100.0% |
| `f1ap_rel18.6_specs` | 22.15 MB | 103.17 MB | 104.5% | 102.0% |
| `ngap_rel18.6_specs` | 19.42 MB | 74.32 MB | 105.6% | 100.0% |
| `lteNRRCC` | 48.50 MB | 65.86 MB | 100.0% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0348s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0944s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0656s | -0.0007s | improved |
| `lteNRRCC` | 0.1280s | 0.1270s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.81 MB | 21.4% | 107.1% |
| `f1ap_rel18.6_specs` | 34.67 MB | 164.52 MB | 103.2% | 103.5% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.44 MB | 103.8% | 102.3% |
| `lteNRRCC` | 74.55 MB | 102.74 MB | 103.2% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0218s | 0.0234s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0817s | 0.0676s | +0.0141s | worse |
| `ngap_rel18.6_specs` | 0.0574s | 0.0466s | +0.0108s | worse |
| `lteNRRCC` | 0.0826s | 0.0773s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.94 MB | 5.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 4.30 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.95 MB | 4.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.72 MB | 4.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0383s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1065s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0754s | +0.0028s | worse |
| `lteNRRCC` | 0.1275s | 0.1380s | -0.0105s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 8.37 MB | 0.0% | 223.1% |
| `f1ap_rel18.6_specs` | 8.97 MB | 8.97 MB | 115.7% | 115.6% |
| `ngap_rel18.6_specs` | 8.42 MB | 7.54 MB | 113.8% | 113.9% |
| `lteNRRCC` | 8.53 MB | 8.65 MB | 227.9% | 115.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0386s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.1309s | 0.1125s | +0.0184s | worse |
| `ngap_rel18.6_specs` | 0.0891s | 0.0757s | +0.0134s | worse |
| `lteNRRCC` | 0.1331s | 0.1363s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.15 MB | 10.40 MB | 0.0% | 215.7% |
| `f1ap_rel18.6_specs` | 11.00 MB | 122.20 MB | 101.9% | 223.6% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.41 MB | 111.9% | 114.2% |
| `lteNRRCC` | 72.11 MB | 83.39 MB | 119.0% | 108.3% |
<!-- BENCH_RESULTS_END -->
