param(
    [Parameter(Mandatory = $true)]
    [string]$BinaryPath,

    [Parameter(Mandatory = $true)]
    [string]$Mode,

    [Parameter(Mandatory = $true)]
    [string]$FixturePath,

    [Parameter(Mandatory = $true)]
    [int]$Seconds
)

$stdoutFile = [System.IO.Path]::GetTempFileName()
$stderrFile = [System.IO.Path]::GetTempFileName()

try {
    $proc = Start-Process `
        -FilePath $BinaryPath `
        -ArgumentList @($Mode, "--no-warnings", "--dir", $FixturePath) `
        -NoNewWindow `
        -RedirectStandardOutput $stdoutFile `
        -RedirectStandardError $stderrFile `
        -PassThru

    $peakCpu = 0.0
    $peakRssKb = 0
    $timedOut = $false
    $start = [System.Diagnostics.Stopwatch]::StartNew()
    $lastCpu = 0.0
    $lastTicks = [System.Diagnostics.Stopwatch]::GetTimestamp()
    $freq = [double][System.Diagnostics.Stopwatch]::Frequency

    while (-not $proc.HasExited) {
        $proc.Refresh()
        $rssKb = [int]($proc.PeakWorkingSet64 / 1kb)
        if ($rssKb -gt $peakRssKb) {
            $peakRssKb = $rssKb
        }

        $nowTicks = [System.Diagnostics.Stopwatch]::GetTimestamp()
        $elapsedSec = ($nowTicks - $lastTicks) / $freq
        $currentCpu = $proc.TotalProcessorTime.TotalSeconds
        if ($elapsedSec -gt 0) {
            $cpuPct = (($currentCpu - $lastCpu) / $elapsedSec) * 100.0
            if ($cpuPct -gt $peakCpu) {
                $peakCpu = $cpuPct
            }
        }
        $lastCpu = $currentCpu
        $lastTicks = $nowTicks

        if ($start.Elapsed.TotalSeconds -ge $Seconds) {
            try {
                $proc.Kill()
            } catch {
            }
            $timedOut = $true
            break
        }

        Start-Sleep -Milliseconds 25
    }

    $proc.WaitForExit()
    $proc.Refresh()

    $finalRssKb = [int]($proc.PeakWorkingSet64 / 1kb)
    if ($finalRssKb -gt $peakRssKb) {
        $peakRssKb = $finalRssKb
    }

    if ($peakCpu -le 0 -and $start.Elapsed.TotalSeconds -gt 0) {
        $avgCpu = ($proc.TotalProcessorTime.TotalSeconds / $start.Elapsed.TotalSeconds) * 100.0
        if ($avgCpu -gt $peakCpu) {
            $peakCpu = $avgCpu
        }
    }

    [Console]::WriteLine(
        "peak_cpu={0:N1} peak_rss_kb={1} exit_code={2} timed_out={3}" -f
            $peakCpu,
            $peakRssKb,
            $proc.ExitCode,
            $timedOut.ToString().ToLowerInvariant()
    )
} finally {
    Remove-Item -LiteralPath $stdoutFile, $stderrFile -ErrorAction SilentlyContinue
}
