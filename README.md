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
Generated: 2026-08-31T17:30:35.700131+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0354s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1103s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0743s | +0.0034s | worse |
| `lteNRRCC` | 0.1214s | 0.1182s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.73 MB | 53.55 MB | 79.2% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0197s | 0.0355s | -0.0158s | improved |
| `f1ap_rel18.6_specs` | 0.0548s | 0.0947s | -0.0399s | improved |
| `ngap_rel18.6_specs` | 0.0387s | 0.0667s | -0.0280s | improved |
| `lteNRRCC` | 0.0700s | 0.1296s | -0.0596s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 36.34 MB | 76.5% | 106.2% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.69 MB | 105.6% | 102.9% |
| `ngap_rel18.6_specs` | 18.01 MB | 74.46 MB | 106.7% | 103.8% |
| `lteNRRCC` | 48.75 MB | 66.46 MB | 105.7% | 102.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0254s | +0.0120s | worse |
| `f1ap_rel18.6_specs` | 0.0975s | 0.0789s | +0.0186s | worse |
| `ngap_rel18.6_specs` | 0.0699s | 0.0559s | +0.0140s | worse |
| `lteNRRCC` | 0.1225s | 0.0846s | +0.0379s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 55.71 MB | 88.0% | 103.4% |
| `f1ap_rel18.6_specs` | 34.70 MB | 164.50 MB | 103.3% | 103.4% |
| `ngap_rel18.6_specs` | 24.56 MB | 117.89 MB | 104.0% | 102.2% |
| `lteNRRCC` | 75.01 MB | 102.79 MB | 101.7% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0250s | 0.0249s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0769s | 0.0942s | -0.0173s | improved |
| `ngap_rel18.6_specs` | 0.0548s | 0.0724s | -0.0176s | improved |
| `lteNRRCC` | 0.0876s | 0.1284s | -0.0408s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.25 MB | 4.02 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.03 MB | 5.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.81 MB | 2.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.12 MB | 14.22 MB | 0.0% | 1.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0427s | 0.0327s | +0.0100s | worse |
| `f1ap_rel18.6_specs` | 0.1102s | 0.0899s | +0.0203s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0622s | +0.0166s | worse |
| `lteNRRCC` | 0.1378s | 0.1100s | +0.0278s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.00 MB | 7.90 MB | 0.0% | 90.7% |
| `f1ap_rel18.6_specs` | 8.73 MB | 106.64 MB | 163.1% | 164.3% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.18 MB | 165.0% | 164.1% |
| `lteNRRCC` | 51.84 MB | 70.55 MB | 108.6% | 167.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0433s | 0.0363s | +0.0070s | worse |
| `f1ap_rel18.6_specs` | 0.1268s | 0.1027s | +0.0241s | worse |
| `ngap_rel18.6_specs` | 0.0862s | 0.0744s | +0.0118s | worse |
| `lteNRRCC` | 0.1287s | 0.1140s | +0.0147s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.15 MB | 9.86 MB | 0.0% | 158.1% |
| `f1ap_rel18.6_specs` | 10.53 MB | 136.96 MB | 174.2% | 174.2% |
| `ngap_rel18.6_specs` | 10.09 MB | 9.50 MB | 172.8% | 101.4% |
| `lteNRRCC` | 9.26 MB | 83.04 MB | 112.3% | 111.7% |
<!-- BENCH_RESULTS_END -->
