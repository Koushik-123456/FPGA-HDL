@echo off
REM Installation Helper Script for Iverilog on Windows
REM This script provides step-by-step guidance for installation

SETLOCAL ENABLEDELAYEDEXPANSION

cls
echo.
echo =====================================
echo Icarus Verilog Installation Helper
echo =====================================
echo.
echo This script will help you install Icarus Verilog on Windows.
echo.
echo NETWORK STATUS: Downloads are currently blocked
echo.
echo Options:
echo 1. Manual Installation (Recommended)
echo 2. USB/Portable Media Installation
echo 3. Use Python Simulator (Already Working)
echo 4. View Installation Instructions
echo.

:menu
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto manual
if "%choice%"=="2" goto portable
if "%choice%"=="3" goto python
if "%choice%"=="4" goto instructions
echo Invalid choice. Please try again.
goto menu

:manual
cls
echo.
echo ========== MANUAL INSTALLATION ==========
echo.
echo STEP 1: Download Icarus Verilog
echo   - Open a web browser
echo   - Go to: https://github.com/steveicarus/iverilog/releases
echo   - Download: iverilog-12_0.exe (or latest version)
echo   - Save to: Downloads folder
echo.
echo STEP 2: Run the Installer
echo   - Double-click the .exe file
echo   - Click "Next" through the wizard
echo   - IMPORTANT: Check "Add to PATH" checkbox
echo   - Click "Install"
echo.
echo STEP 3: Verify Installation
echo   - Open Command Prompt or PowerShell
echo   - Run: iverilog -version
echo   - Should display version number
echo.
echo STEP 4: Run Simulations
echo   - Open PowerShell in this folder
echo   - Run: .\scripts\run_iverilog.ps1
echo.
pause
goto menu

:portable
cls
echo.
echo ========== PORTABLE INSTALLATION ==========
echo.
echo If you have Iverilog on USB/External Drive:
echo.
echo STEP 1: Copy Files
echo   - Copy iverilog folder from USB to C:\iverilog
echo.
echo STEP 2: Add to PATH
echo   - Open PowerShell as Administrator
echo   - Run this command:
echo.
echo   [Environment]::SetEnvironmentVariable^("Path", $env:PATH + ";C:\iverilog\bin", [EnvironmentVariableTarget]::User^)
echo.
echo STEP 3: Verify
echo   - Close and reopen PowerShell
echo   - Run: iverilog -version
echo.
pause
goto menu

:python
cls
echo.
echo ========== PYTHON SIMULATOR (ALREADY WORKING!) ==========
echo.
echo Your Python simulator is already fully functional!
echo.
echo To run simulations:
echo   cd "C:\Users\sunka\OneDrive\Desktop\nrml vlsi project"
echo   python scripts/python_sim.py
echo.
echo To view waveforms in browser:
echo   start site/waveforms.html
echo.
echo The HTML viewer displays REAL waveforms from actual test vectors:
echo   - ALU: 21 comprehensive tests
echo   - MUX: 10 test cases
echo   - Counter: Multi-phase testing
echo.
echo All VCD files are generated and accessible!
echo.
pause
goto menu

:instructions
cls
echo.
echo ========== DETAILED INSTALLATION GUIDE ==========
echo.
echo Read the full guide at:
echo   ICARUS_SETUP.md (in project root)
echo.
echo Key points:
echo.
echo REQUIRED: Internet Connection for download
echo   - https://github.com/steveicarus/iverilog/releases
echo.
echo INSTALLATION TIME: 5-10 minutes
echo.
echo VERIFICATION: Run these commands
echo   iverilog -version
echo   vvp -version
echo.
echo AUTOMATION: PowerShell script ready
echo   .\scripts\run_iverilog.ps1
echo.
echo VIEWING RESULTS:
echo   gtkwave wave/alu_4bit.vcd
echo   gtkwave wave/mux4to1.vcd
echo   gtkwave wave/counter3.vcd
echo.
echo.
echo CURRENT STATUS:
echo   ✓ Testbenches created (21 ALU, 10 MUX, 10 Counter tests)
echo   ✓ PowerShell automation script ready
echo   ✓ GNU Makefile ready
echo   ✓ VCD files will be generated after installation
echo.
pause
goto menu
