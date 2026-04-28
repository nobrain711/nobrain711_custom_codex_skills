param(
    [string] $ProjectRoot
)

$ErrorActionPreference = "Stop"

function Get-IsoWeekInfo {
    param(
        [datetime] $Date
    )

    $day = [int] $Date.DayOfWeek
    if ($day -eq 0) {
        $day = 7
    }

    $thursday = $Date.Date.AddDays(4 - $day)
    $isoYear = $thursday.Year
    $firstThursday = [datetime]::new($isoYear, 1, 4)
    $firstDay = [int] $firstThursday.DayOfWeek
    if ($firstDay -eq 0) {
        $firstDay = 7
    }

    $firstIsoThursday = $firstThursday.AddDays(4 - $firstDay)
    $isoWeek = 1 + [int] [Math]::Floor(($thursday - $firstIsoThursday).TotalDays / 7)

    [pscustomobject]@{
        Year = $isoYear
        Week = $isoWeek
    }
}

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    $ProjectRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..\..\..\..")
} else {
    $ProjectRoot = Resolve-Path -LiteralPath $ProjectRoot
}

$logPath = Join-Path $ProjectRoot "log.md"
if (-not (Test-Path -LiteralPath $logPath)) {
    $header = "# Chat Log`r`n`r`nActive project chat log. Weekly archives are stored under logs/<year>/W<number>.md.`r`n"
    Set-Content -LiteralPath $logPath -Value $header -Encoding utf8
    return
}

$content = Get-Content -LiteralPath $logPath -Raw -Encoding utf8
if ([string]::IsNullOrWhiteSpace($content)) {
    return
}

$archiveDate = (Get-Date).AddDays(-1)
$archiveInfo = Get-IsoWeekInfo -Date $archiveDate
$archiveYear = $archiveInfo.Year
$archiveWeek = $archiveInfo.Week
$weekName = "W{0:D2}.md" -f $archiveWeek
$archiveDir = Join-Path $ProjectRoot (Join-Path "logs" $archiveYear)
$archivePath = Join-Path $archiveDir $weekName

New-Item -ItemType Directory -Path $archiveDir -Force | Out-Null

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss zzz"
$entry = "## Archived at $timestamp`r`n`r`n$content.Trim()`r`n"

if (Test-Path -LiteralPath $archivePath) {
    Add-Content -LiteralPath $archivePath -Value "`r`n---`r`n`r`n$entry" -Encoding utf8
} else {
    Set-Content -LiteralPath $archivePath -Value "# Chat Log Archive - $archiveYear $weekName`r`n`r`n$entry" -Encoding utf8
}

$newHeader = @"
# Chat Log

Active project chat log. Weekly archives are stored under `logs/<year>/W<number>.md`.

"@

Set-Content -LiteralPath $logPath -Value $newHeader -Encoding utf8
