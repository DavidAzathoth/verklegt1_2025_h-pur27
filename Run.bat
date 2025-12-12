@echo off
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
	py "%~dp0main.py"
) else (
	where python >nul 2>nul
	if %errorlevel%==0 (
		python "%~dp0main.py"
	) else (
		echo ERROR: Python not found. Install Python or add it to PATH
		pause
		exit /b 1
	)
)
