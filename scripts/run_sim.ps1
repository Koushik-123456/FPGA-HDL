param(
    [string]$which = "all"
)

$iverilog = "iverilog"
$vvp = "vvp"
$python = "python"

function Run-Iverilog($name, $tb, $src) {
    $out = "wave/$name.vvp"
    Write-Host "Compiling $tb + $src -> $out (Icarus Verilog)"
    & $iverilog -o $out $tb $src
    if ($LASTEXITCODE -ne 0) { Write-Error "Compilation failed"; exit $LASTEXITCODE }
    & $vvp $out
}

function Run-Python($name) {
    Write-Host "Running simulation: $name (Python)"
    & $python scripts/python_sim.py $name
    if ($LASTEXITCODE -ne 0) { Write-Error "Python simulation failed"; exit $LASTEXITCODE }
}

function Run-One($name, $tb, $src) {
    if (Get-Command $iverilog -ErrorAction SilentlyContinue) {
        Run-Iverilog $name $tb $src
    } else {
        Write-Host "iverilog not found, using Python simulator..."
        Run-Python $name
    }
}

switch ($which) {
    "alu" { Run-One alu tb/alu_4bit_tb.v src/alu_4bit.v }
    "mux" { Run-One mux tb/mux4to1_tb.v src/mux4to1.v }
    "counter" { Run-One counter tb/counter3_tb.v src/counter3.v }
    default {
        Run-One alu tb/alu_4bit_tb.v src/alu_4bit.v
        Run-One mux tb/mux4to1_tb.v src/mux4to1.v
        Run-One counter tb/counter3_tb.v src/counter3.v
    }
}
