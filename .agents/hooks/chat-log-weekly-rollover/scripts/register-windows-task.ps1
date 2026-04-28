param(
    [string] $TaskName = "Codex Chat Log Weekly Rollover",
    [string] $ProjectRoot
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    $ProjectRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..\..\..\..")
} else {
    $ProjectRoot = Resolve-Path -LiteralPath $ProjectRoot
}

$scriptPath = Join-Path $ProjectRoot ".agents\hooks\chat-log-weekly-rollover\scripts\rollover-chat-log.ps1"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Rollover script not found: $scriptPath"
}

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" -ProjectRoot `"$ProjectRoot`""

$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 12:00am
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Archive project log.md into logs/<year>/W<number>.md every Monday at 00:00." `
    -Force | Out-Null

Write-Host "Registered scheduled task: $TaskName"
