@@:: ===================================================================
@@::  RESTYLE_REEL.cmd  -  raise the subtitles so they clear the desk graphic.
@@::  Reuses _stitched.mp4 + subs.srt. No re-transcribing. Double-click it.
@@:: ===================================================================
@@echo off
@@findstr /v "^@@" "%~f0" > "%TEMP%\_Restyle.ps1"
@@powershell -NoProfile -ExecutionPolicy Bypass -File "%TEMP%\_Restyle.ps1" -HintFolder "%~dp0."
@@echo.
@@pause
@@exit /b
param(
  [string]$HintFolder = "",
  [string]$OutName    = "Reel_master_subbed.mp4",
  [int]   $FontSize   = 60,
  [int]   $Outline    = 4,
  [string]$FontName   = "Arial",
  [double]$PreviewAt  = 7.0
)

$ErrorActionPreference = "Continue"
function Say($m){ Write-Host "`n=== $m ===" -ForegroundColor Cyan }
function Die($m){ Write-Host "`nERROR: $m" -ForegroundColor Red; exit 1 }

# A fresh cmd window inherits PATH from Explorer, which can still be stale after
# a winget install. Re-read it from the registry, then go looking by hand.
function Refresh-Path {
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
              [System.Environment]::GetEnvironmentVariable("Path","User")
}
function Find-Exe([string]$name) {
  $c = Get-Command $name -EA SilentlyContinue
  if ($c) { return $c.Source }
  Refresh-Path
  $c = Get-Command $name -EA SilentlyContinue
  if ($c) { return $c.Source }
  $roots = @("$env:LOCALAPPDATA\Microsoft\WinGet\Packages",
             "$env:LOCALAPPDATA\Microsoft\WinGet\Links",
             "$env:ProgramFiles", "$env:ProgramData\chocolatey")
  foreach ($r in $roots) {
    if (-not (Test-Path -LiteralPath $r)) { continue }
    $hit = Get-ChildItem -Path $r -Filter "$name.exe" -Recurse -File -EA SilentlyContinue | Select-Object -First 1
    if ($hit) { return $hit.FullName }
  }
  return $null
}

# ---------- find the working files ----------
Say "Looking for _stitched.mp4 and subs.srt"
$dirs = @()
if ($HintFolder) { $dirs += $HintFolder }
$dirs += "$env:USERPROFILE\Downloads","$env:USERPROFILE\Desktop",(Get-Location).Path
$Folder = $null
foreach ($d in $dirs) {
  if (-not (Test-Path -LiteralPath $d)) { continue }
  if ((Test-Path -LiteralPath (Join-Path $d "_stitched.mp4")) -and (Test-Path -LiteralPath (Join-Path $d "subs.srt"))) {
    $Folder = (Resolve-Path -LiteralPath $d).Path; break
  }
}
if (-not $Folder) { Die "Could not find _stitched.mp4 and subs.srt. Run MAKE_REEL.cmd first." }
Set-Location -LiteralPath $Folder
Write-Host "Working in: $Folder" -ForegroundColor Green

$FF = Find-Exe "ffmpeg"
$FP = Find-Exe "ffprobe"
if (-not $FF) { Die "Could not find ffmpeg.exe anywhere. Run MAKE_REEL.cmd once to install it." }
if (-not $FP) { Die "Could not find ffprobe.exe anywhere. Run MAKE_REEL.cmd once to install it." }
Write-Host "ffmpeg: $FF" -ForegroundColor DarkGray

# ---------- build an .ass at a given height ----------
# an .srt carries no resolution, so libass would assume 384x288 and render the
# text ~6x too large in mid-frame. Pin the canvas to the real 1080x1920.
function Build-Ass([int]$MarginV, [string]$outFile) {
  & $FF -y -hide_banner -loglevel error -i "subs.srt" "_tmp_raw.ass"
  if ($LASTEXITCODE -ne 0) { Die "SRT -> ASS conversion failed." }
  $style = "Style: Default,$FontName,$FontSize,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,$Outline,0,2,60,60,$MarginV,1"
  $a = Get-Content "_tmp_raw.ass" -Raw
  $a = $a -replace '(?m)^PlayResX:.*$', 'PlayResX: 1080'
  $a = $a -replace '(?m)^PlayResY:.*$', 'PlayResY: 1920'
  $a = $a -replace '(?m)^Style: Default,.*$', $style
  if ($a -notmatch 'PlayResX: 1080') { Die "Could not pin the subtitle canvas." }
  Set-Content -LiteralPath $outFile -Value $a -Encoding UTF8
}

# ---------- 1. three previews, seconds each ----------
Say "Rendering previews"
$options = @(300, 420, 540)
foreach ($m in $options) {
  Build-Ass $m "_preview_$m.ass"
  & $FF -y -hide_banner -loglevel error -ss $PreviewAt -i "_stitched.mp4" `
    -vf "ass=_preview_$m.ass" -frames:v 1 "preview_margin_$m.png"
  Write-Host ("  preview_margin_{0}.png   ({0} px above the bottom edge)" -f $m)
}

Write-Host ""
Write-Host "Open those 3 PNGs in this folder and see which one clears the desk graphic." -ForegroundColor Yellow
Write-Host "  300 = a little higher than now (was 150)"
Write-Host "  420 = clears the TLV NEWS ROOM band"
Write-Host "  540 = well above it"
Write-Host ""
$pick = Read-Host "Type 300, 420 or 540 (or any other number you prefer)"
$MarginV = 0
if (-not [int]::TryParse($pick.Trim(), [ref]$MarginV) -or $MarginV -lt 0 -or $MarginV -gt 1500) {
  Die "Not a usable number. Run this again and type e.g. 420."
}

# ---------- 2. keep the old master, never overwrite ----------
if (Test-Path -LiteralPath $OutName) {
  $base = [IO.Path]::GetFileNameWithoutExtension($OutName)
  $old  = "${base}_old.mp4"
  $n = 2
  while (Test-Path -LiteralPath $old) { $old = "${base}_old$n.mp4"; $n++ }
  Rename-Item -LiteralPath $OutName -NewName $old
  Write-Host "Previous master kept as: $old" -ForegroundColor DarkGray
}

# ---------- 3. burn ----------
Say "Burning at MarginV = $MarginV"
Build-Ass $MarginV "subs.ass"
& $FF -y -hide_banner -loglevel warning -stats -i "_stitched.mp4" -vf "ass=subs.ass" `
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -r 30 `
  -c:a aac -b:a 192k -movflags +faststart "$OutName"
if ($LASTEXITCODE -ne 0) { Die "Burn failed." }

# ---------- 4. verify ----------
Say "Verifying"
function Get-Dur($f){ [double](& $FP -v error -show_entries format=duration -of csv=p=0 -- "$f") }
$dur     = Get-Dur $OutName
$streams = & $FP -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate -of csv=p=0 -- "$OutName"
$hasAudio = ($streams -join "`n") -match "audio"
foreach ($p in @(@(7.0,"frame_clip1.png"), @(($dur-3.5),"frame_clip2.png"))) {
  & $FF -y -hide_banner -loglevel error -ss $p[0] -i "$OutName" -frames:v 1 $p[1]
}

Write-Host "`nDONE" -ForegroundColor Green
Write-Host ("  file      : {0}" -f (Resolve-Path $OutName))
Write-Host ("  size      : {0:N2} MB" -f ((Get-Item $OutName).Length/1MB))
Write-Host ("  duration  : {0:N3}s" -f $dur)
Write-Host ("  audio     : {0}" -f $(if($hasAudio){"PASS"}else{"FAIL - no audio"}))
$streams | ForEach-Object { Write-Host "      $_" }
Write-Host "  check     : frame_clip1.png / frame_clip2.png"
