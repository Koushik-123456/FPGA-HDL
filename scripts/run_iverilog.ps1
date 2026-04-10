# Icarus Verilog Simulation Script for Windows
# Usage: ./run_iverilog.ps1
# Prerequisites: iverilog and vvp installed and in PATH

param(
    [string]$Module = "all"  # all, alu, mux, or counter
)

$projectRoot = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$srcDir = Join-Path $projectRoot "src"
$tbDir = Join-Path $projectRoot "tb"
$buildDir = Join-Path $projectRoot "build"
$waveDir = Join-Path $projectRoot "wave"

# Create directories
if (!(Test-Path $buildDir)) { New-Item -ItemType Directory -Path $buildDir | Out-Null }
if (!(Test-Path $waveDir)) { New-Item -ItemType Directory -Path $waveDir | Out-Null }

Write-Host "⚙️  Icarus Verilog Simulation Suite" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Function to compile and run simulation
function Run-Simulation {
    param(
        [string]$ModuleName,
        [string]$ModuleFile,
        [string]$TestbenchFile,
        [string]$VCDFile
    )
    
    $vvpFile = Join-Path $buildDir "$ModuleName.vvp"
    $vcdPath = Join-Path $waveDir $VCDFile
    
    Write-Host "Module: $ModuleName" -ForegroundColor Yellow
    Write-Host "  Compiling..." -NoNewline
    
    # Compile Verilog modules
    $moduleFullPath = Join-Path $srcDir $ModuleFile
    $tbFullPath = Join-Path $tbDir $TestbenchFile
    
    & iverilog -o $vvpFile $moduleFullPath $tbFullPath 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host " ✓" -ForegroundColor Green
    } else {
        Write-Host " ✗" -ForegroundColor Red
        Write-Host "  Compilation failed!" -ForegroundColor Red
        return $false
    }
    
    Write-Host "  Running simulation..." -NoNewline
    
    # Run simulation and generate VCD
    & vvp $vvpFile -vcd $vcdPath 2>&1 | Out-Null
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host " ✓" -ForegroundColor Green
        $fileSize = (Get-Item $vcdPath).Length
        Write-Host "  VCD generated: $(Split-Path -Leaf $vcdPath) ($fileSize bytes)" -ForegroundColor Green
        return $true
    } else {
        Write-Host " ✗" -ForegroundColor Red
        return $false
    }
}

# Run selected modules
$results = @()

switch ($Module.ToLower()) {
    "all" {
        $results += @(Run-Simulation "ALU 4-bit" "alu_4bit.v" "alu_4bit_tb.v" "alu_4bit.vcd")
        Write-Host ""
        $results += @(Run-Simulation "MUX 4-to-1" "mux4to1.v" "mux4to1_tb.v" "mux4to1.vcd")
        Write-Host ""
        $results += @(Run-Simulation "Counter 3-bit" "counter3.v" "counter3_tb.v" "counter3.vcd")
    }
    "alu" {
        $results += @(Run-Simulation "ALU 4-bit" "alu_4bit.v" "alu_4bit_tb.v" "alu_4bit.vcd")
    }
    "mux" {
        $results += @(Run-Simulation "MUX 4-to-1" "mux4to1.v" "mux4to1_tb.v" "mux4to1.vcd")
    }
    "counter" {
        $results += @(Run-Simulation "Counter 3-bit" "counter3.v" "counter3_tb.v" "counter3.vcd")
    }
    default {
        Write-Host "Unknown module: $Module" -ForegroundColor Red
        Write-Host "Valid options: all, alu, mux, counter" -ForegroundColor Yellow
        exit 1
    }
}

# Summary
Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
$passCount = ($results | Where-Object { $_ -eq $true }).Count
$totalCount = $results.Count
Write-Host "Results: $passCount/$totalCount modules simulated" -ForegroundColor $(if($passCount -eq $totalCount) { "Green" } else { "Yellow" })
Write-Host ""

if ($passCount -eq $totalCount) {
    Write-Host "✓ All simulations completed successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "View waveforms with GTKWave:" -ForegroundColor Cyan
    Write-Host "  gtkwave wave/alu_4bit.vcd" -ForegroundColor Gray
    Write-Host "  gtkwave wave/mux4to1.vcd" -ForegroundColor Gray
    Write-Host "  gtkwave wave/counter3.vcd" -ForegroundColor Gray
    exit 0
} else {
    Write-Host "✗ Some simulations failed!" -ForegroundColor Red
    exit 1
}
