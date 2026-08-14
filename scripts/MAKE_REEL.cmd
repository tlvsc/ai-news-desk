@@:: ===================================================================
@@::  MAKE_REEL.cmd  -  double-click this. One file. Installs what it needs.
@@:: ===================================================================
@@echo off
@@findstr /v "^@@" "%~f0" > "%TEMP%\_MakeReel.ps1"
@@powershell -NoProfile -ExecutionPolicy Bypass -File "%TEMP%\_MakeReel.ps1" -HintFolder "%~dp0."
@@echo.
@@pause
@@exit /b
param(
  [string]$HintFolder = "",
  [string]$Clip1      = "MiniMax_H3_00070_.mp4",
  [string]$Clip2      = "MiniMax_H3_00073_.mp4",
  [string]$OutName    = "Reel_master_subbed.mp4",
  [double]$Fade       = 0.5,
  [int]   $MarginV    = 150,
  [int]   $FontSize   = 60,
  [int]   $Outline    = 4,
  [string]$FontName   = "Arial",
  [string]$Model      = "small"
)

$ErrorActionPreference = "Continue"
function Say($m){ Write-Host "`n=== $m ===" -ForegroundColor Cyan }
function Die($m){ Write-Host "`nERROR: $m" -ForegroundColor Red; exit 1 }

function Refresh-Path {
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
              [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Windows ships a fake python.exe that just opens the Microsoft Store, so
# "does python exist" is not the question - "does python actually RUN" is.
function Test-RealPython($exe) {
  if (-not $exe) { return $false }
  try {
    $out = & $exe -c "print(42)" 2>$null
    return ($LASTEXITCODE -eq 0 -and "$out".Trim() -eq "42")
  } catch { return $false }
}

function Find-Python {
  # the py launcher can tell us where the real interpreter lives
  try {
    $p = & py -3 -c "import sys; print(sys.executable)" 2>$null
    if ($LASTEXITCODE -eq 0 -and $p -and (Test-RealPython $p.Trim())) { return $p.Trim() }
  } catch {}

  # plain python, but only if it genuinely runs (not the Store stub)
  $c = (Get-Command python -EA SilentlyContinue)
  if ($c -and (Test-RealPython $c.Source)) { return $c.Source }

  # known install locations
  $globs = @(
    "$env:LOCALAPPDATA\Programs\Python\Python3*\python.exe",
    "$env:ProgramFiles\Python3*\python.exe",
    "${env:ProgramFiles(x86)}\Python3*\python.exe",
    "C:\Python3*\python.exe"
  )
  foreach ($g in $globs) {
    foreach ($f in (Get-ChildItem -Path $g -EA SilentlyContinue | Sort-Object FullName -Descending)) {
      if (Test-RealPython $f.FullName) { return $f.FullName }
    }
  }
  return $null
}

# ---------- 0. Find the clips ----------
Say "Looking for the clips"
$searchDirs = @()
if ($HintFolder) { $searchDirs += $HintFolder }
$searchDirs += "$env:USERPROFILE\Downloads","$env:USERPROFILE\Desktop","$env:USERPROFILE\Videos",(Get-Location).Path

$Folder = $null
foreach ($d in $searchDirs) {
  if (-not (Test-Path -LiteralPath $d)) { continue }
  if ((Test-Path -LiteralPath (Join-Path $d $Clip1)) -and (Test-Path -LiteralPath (Join-Path $d $Clip2))) {
    $Folder = (Resolve-Path -LiteralPath $d).Path; break
  }
}
if (-not $Folder) {
  $hit = Get-ChildItem -Path $env:USERPROFILE -Filter $Clip1 -Recurse -File -EA SilentlyContinue | Select-Object -First 1
  if ($hit -and (Test-Path -LiteralPath (Join-Path $hit.DirectoryName $Clip2))) { $Folder = $hit.DirectoryName }
}
if (-not $Folder) { Die "Could not find both clips. Put them in Downloads and run again." }
Set-Location -LiteralPath $Folder
Write-Host "Found both clips in: $Folder" -ForegroundColor Green

# ---------- 1. ffmpeg ----------
Say "Step 1 - ffmpeg"
if (-not (Get-Command ffmpeg -EA SilentlyContinue)) {
  Write-Host "Installing ffmpeg..."
  winget install --id Gyan.FFmpeg -e --accept-source-agreements --accept-package-agreements --silent
  Refresh-Path
}
if (-not (Get-Command ffmpeg -EA SilentlyContinue)) { Die "ffmpeg not on PATH. Close this window and run MAKE_REEL.cmd again." }
Write-Host ("ffmpeg  : " + ((ffmpeg -version 2>&1 | Select-Object -First 1)))

# ---------- 2. Python + whisper ----------
Say "Step 2 - Python + Whisper"
$PY = Find-Python
if (-not $PY) {
  Write-Host "No working Python found (the one on PATH is the Microsoft Store stub)."
  Write-Host "Installing real Python - a few minutes..." -ForegroundColor Yellow
  winget install --id Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements --silent
  Refresh-Path
  $PY = Find-Python
}
if (-not $PY) {
  Write-Host "`nPython installed but still not usable in this window." -ForegroundColor Yellow
  Write-Host "Close this window and double-click MAKE_REEL.cmd again." -ForegroundColor Yellow
  exit 1
}
Write-Host ("python  : " + $PY)
Write-Host ("version : " + (& $PY --version 2>&1))

# torch ships DLLs that need the Microsoft C++ runtime. Without it you get a
# DLL load failure at "import torch". Idempotent - skips if already present.
Write-Host "Checking Microsoft Visual C++ Redistributable..."
winget install --id Microsoft.VCRedist.2015+.x64 -e --accept-source-agreements --accept-package-agreements --silent 2>&1 | Out-Null

& $PY -c "import whisper" 2>$null
if ($LASTEXITCODE -ne 0) {
  Write-Host "Installing Whisper - about 2 GB the first time. Leave this running." -ForegroundColor Yellow
  & $PY -m pip install --upgrade pip --quiet
  & $PY -m pip install openai-whisper
}

# final check, and if it still fails SHOW WHY instead of guessing
$importErr = (& $PY -c "import whisper" 2>&1) | Out-String
if ($LASTEXITCODE -ne 0) {
  Write-Host "`nWhisper is installed but will not load. The real error:" -ForegroundColor Red
  Write-Host $importErr
  if ($importErr -match "DLL load failed|_C\b|MSVC|VCRUNTIME") {
    Write-Host "That is the missing C++ runtime." -ForegroundColor Yellow
    Write-Host "Install it manually from: https://aka.ms/vs/17/release/vc_redist.x64.exe" -ForegroundColor Yellow
    Write-Host "Then run MAKE_REEL.cmd again." -ForegroundColor Yellow
  }
  exit 1
}
Write-Host "whisper : OK"

# ---------- 3. Stitch ----------
Say "Step 3 - stitching with a $Fade s crossfade"
function Get-Dur($f){ [double](ffprobe -v error -show_entries format=duration -of csv=p=0 -- "$f") }
$d1 = Get-Dur $Clip1
$d2 = Get-Dur $Clip2
$offset = [math]::Round($d1 - $Fade, 3)
Write-Host ("clip1 = {0:N3}s   clip2 = {1:N3}s" -f $d1,$d2)
if ($offset -le 0) { Die "clip1 is shorter than the crossfade." }

$norm = "scale=1080:1920:force_original_aspect_ratio=decrease," +
        "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps=30"
$fc = "[0:v]$norm[v0];[1:v]$norm[v1];" +
      "[v0][v1]xfade=transition=fade:duration=$Fade`:offset=$offset,format=yuv420p[v];" +
      "[0:a][1:a]acrossfade=d=$Fade`:c1=tri:c2=tri[a]"

ffmpeg -y -hide_banner -loglevel warning -stats -i "$Clip1" -i "$Clip2" `
  -filter_complex $fc -map "[v]" -map "[a]" `
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -r 30 `
  -c:a aac -b:a 192k -movflags +faststart "_stitched.mp4"
if ($LASTEXITCODE -ne 0) { Die "Stitch failed." }

# ---------- 4. Transcribe ----------
Say "Step 4 - transcribing (first run also downloads the model)"
ffmpeg -y -hide_banner -loglevel error -i "_stitched.mp4" -vn -ac 1 -ar 16000 "_audio.wav"
if ($LASTEXITCODE -ne 0) { Die "Audio extract failed." }
& $PY -m whisper "_audio.wav" --model $Model --language English --task transcribe --output_format srt --output_dir . --verbose False
if ($LASTEXITCODE -ne 0) { Die "Whisper failed." }
if (-not (Test-Path "_audio.srt")) { Die "Whisper produced no SRT." }
Copy-Item "_audio.srt" "subs.srt" -Force

# ---------- 5. PAUSE for approval ----------
Say "Step 5 - READ THE SUBTITLES"
Write-Host "------------------------------------------------------------"
Get-Content "subs.srt" | Write-Host
Write-Host "------------------------------------------------------------`n"
Write-Host "Wrong words? Open  subs.srt  in Notepad, fix the TEXT only," -ForegroundColor Yellow
Write-Host "leave the numbers and timestamps alone, save, then come back." -ForegroundColor Yellow
Write-Host ""
$ans = Read-Host "Type  yes  to burn them in (anything else stops)"
if ($ans.Trim().ToLower() -ne "yes") { Write-Host "Stopped. _stitched.mp4 and subs.srt are kept."; exit 0 }

# ---------- 6. Burn ----------
Say "Step 6 - burning subtitles"
# an .srt carries no resolution, so libass would assume 384x288 and render the
# text ~6x too large in mid-frame. Convert to .ass and pin the canvas to 1080x1920.
ffmpeg -y -hide_banner -loglevel error -i "subs.srt" "_subs_raw.ass"
if ($LASTEXITCODE -ne 0) { Die "SRT -> ASS conversion failed." }
$styleLine = "Style: Default,$FontName,$FontSize,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,$Outline,0,2,60,60,$MarginV,1"
$ass = Get-Content "_subs_raw.ass" -Raw
$ass = $ass -replace '(?m)^PlayResX:.*$', 'PlayResX: 1080'
$ass = $ass -replace '(?m)^PlayResY:.*$', 'PlayResY: 1920'
$ass = $ass -replace '(?m)^Style: Default,.*$', $styleLine
if ($ass -notmatch 'PlayResX: 1080') { Die "Could not pin the subtitle canvas - stopping rather than burning giant text." }
Set-Content -LiteralPath "subs.ass" -Value $ass -Encoding UTF8

ffmpeg -y -hide_banner -loglevel warning -stats -i "_stitched.mp4" -vf "ass=subs.ass" `
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -r 30 `
  -c:a aac -b:a 192k -movflags +faststart "$OutName"
if ($LASTEXITCODE -ne 0) { Die "Burn failed." }

# ---------- 7. Verify ----------
Say "Step 7 - verifying"
$expected = [math]::Round($d1 + $d2 - $Fade, 3)
$actual   = Get-Dur $OutName
$delta    = [math]::Abs($actual - $expected)
$streams  = ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate -of csv=p=0 -- "$OutName"
$hasAudio = ($streams -join "`n") -match "audio"
$f1    = [math]::Round($d1/2, 2)
$fJoin = [math]::Round($d1 - ($Fade/2), 2)
$f2    = [math]::Round($d1 + ($d2/2) - $Fade, 2)
foreach ($p in @(@($f1,"frame_clip1.png"), @($fJoin,"frame_join.png"), @($f2,"frame_clip2.png"))) {
  ffmpeg -y -hide_banner -loglevel error -ss $p[0] -i "$OutName" -frames:v 1 $p[1]
}

Write-Host "`nDONE" -ForegroundColor Green
Write-Host ("  file      : {0}" -f (Resolve-Path $OutName))
Write-Host ("  size      : {0:N2} MB" -f ((Get-Item $OutName).Length/1MB))
Write-Host ("  duration  : {0:N3}s (expected {1:N3}s)  {2}" -f $actual,$expected,$(if($delta -lt 0.15){"PASS"}else{"CHECK"}))
Write-Host ("  audio     : {0}" -f $(if($hasAudio){"PASS"}else{"FAIL - no audio"}))
$streams | ForEach-Object { Write-Host "      $_" }
Write-Host "`nSend me frame_clip1.png / frame_join.png / frame_clip2.png and I'll check them." -ForegroundColor Yellow
