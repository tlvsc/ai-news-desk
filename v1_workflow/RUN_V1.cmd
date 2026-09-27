@echo off
setlocal EnableExtensions
rem AI News Desk V1 workflow (Claude lane). Double-click to run today's edition.
rem House rule 13: check that Python RUNS (the Microsoft Store stub only opens the Store), never that it merely exists.
cd /d "%~dp0"
set "PY="
for %%C in ("py -3" "python" "python3") do (
  if not defined PY (
    %%~C -c "import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)" >nul 2>&1
    if not errorlevel 1 set "PY=%%~C"
  )
)
if not defined PY (
  echo.
  echo Python 3.11 or newer was not found, or python.exe is the Microsoft Store stub.
  echo Install it from https://www.python.org/downloads/windows/  and tick "Add python.exe to PATH".
  echo After installing, close this window and double-click RUN_V1.cmd again (PATH is stale until then).
  start "" https://www.python.org/downloads/windows/
  pause
  exit /b 1
)
echo Using: %PY%
%PY% -c "import sys; print('Python', sys.version.split()[0])"
echo.
echo Nothing else is installed: the workflow uses the Python standard library only.
echo LLM stages call the Claude Code CLI (claude) on Rafael's subscription; ffmpeg and ComfyUI are used only by s15 and s16.
echo.
set "ARGS=%*"
if "%ARGS%"=="" set "ARGS=--edition today --run-description "double-click run""
%PY% run_v1.py %ARGS%
set "RC=%errorlevel%"
echo.
if "%RC%"=="0" echo DONE. Read runs\^<date^>\V1_script_report.md for the evidence.
if "%RC%"=="2" echo STOPPED: a gate failed. Read runs\^<date^>\V1_script_report.md. Rafael may override with --override gate=reason.
if "%RC%"=="3" echo PAUSED: approval needed. Read runs\^<date^>\approvals\*.pending.md then run: RUN_V1.cmd --edition ^<date^> --approve ^<stage^>
if "%RC%"=="4" echo PAUSED: this step needs the production PC or a tool (ComfyUI, ffmpeg, the card renderer). See the *_PENDING.md file named in the log.
if "%RC%"=="1" echo ERROR: see runs\^<date^>\work\run.log
pause
exit /b %RC%
