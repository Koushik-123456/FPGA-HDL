# Icarus Verilog Installation & Setup Guide for Windows

## Overview
This guide provides step-by-step instructions to install and use Icarus Verilog (iverilog) on Windows for this FPGA HDL verification project.

## Option 1: Install via Package Manager (Recommended)

### Prerequisites
You need one of these package managers installed:
- **Chocolatey** (https://chocolatey.org/install)
- **Scoop** (https://scoop.sh/#installation)

### Installation Steps

**With Chocolatey:**
```powershell
# Run as Administrator
choco install iverilog -y
```

**With Scoop:**
```powershell
scoop install iverilog
```

**Verify Installation:**
```powershell
iverilog -version
vvp -version
```

---

## Option 2: Manual Download (If package manager unavailable)

### Step 1: Download Installer
1. Go to [Icarus Verilog Releases](https://github.com/steveicarus/iverilog/releases)
2. Download the latest `.exe` installer for Windows (e.g., `iverilog-12_0.exe`)
3. Save to your Downloads folder

### Step 2: Install
1. Double-click the downloaded `.exe` file
2. Follow the installer wizard
3. **Important**: When prompted, choose to add to PATH
4. Default installation path: `C:\iverilog`

### Step 3: Verify Installation
Open PowerShell and run:
```powershell
iverilog -version
vvp -version
```

Should display version info without errors.

---

## Option 3: Pre-compiled Portable Version (No Installation)

If standard installation doesn't work:

1. Download portable binaries from [iverilog-win64](https://github.com/yurivich/iverilog-win64)
2. Extract to `C:\iverilog`
3. Add to PATH manually:
   ```powershell
   $env:PATH += ";C:\iverilog\bin"
   [Environment]::SetEnvironmentVariable("Path", $env:PATH, [EnvironmentVariableTarget]::User)
   ```

---

## Running Simulations

Once installed, use the provided PowerShell script:

### Run All Simulations
```powershell
cd "C:\Users\sunka\OneDrive\Desktop\nrml vlsi project"
.\scripts\run_iverilog.ps1
```

### Run Specific Module
```powershell
# ALU only
.\scripts\run_iverilog.ps1 -Module alu

# MUX only
.\scripts\run_iverilog.ps1 -Module mux

# Counter only
.\scripts\run_iverilog.ps1 -Module counter
```

---

## Manual Compilation & Execution

If you prefer command-line control:

### Compile & Simulate ALU
```powershell
cd "C:\Users\sunka\OneDrive\Desktop\nrml vlsi project"

# Compile
iverilog -o build/alu_4bit.vvp src/alu_4bit.v tb/alu_4bit_tb.v

# Run simulation and generate VCD
vvp build/alu_4bit.vvp -vcd wave/alu_4bit.vcd
```

### Compile & Simulate MUX
```powershell
iverilog -o build/mux4to1.vvp src/mux4to1.v tb/mux4to1_tb.v
vvp build/mux4to1.vvp -vcd wave/mux4to1.vcd
```

### Compile & Simulate Counter
```powershell
iverilog -o build/counter3.vvp src/counter3.v tb/counter3_tb.v
vvp build/counter3.vvp -vcd wave/counter3.vcd
```

---

## View Waveforms

### With GTKWave
```powershell
# If GTKWave is installed:
gtkwave wave/alu_4bit.vcd
gtkwave wave/mux4to1.vcd
gtkwave wave/counter3.vcd
```

### With HTML Viewer (No external tools needed)
```powershell
# Open in browser
start site/waveforms.html
```

---

## Troubleshooting

### "iverilog: command not found"
**Solution**: 
- Add to PATH environment variable
- In PowerShell: `$env:PATH += ";C:\iverilog\bin"`
- Or add permanently in Windows System Properties → Environment Variables

### Compilation Error: "Cannot find module"
**Solution**: Ensure you're in the project root directory and paths match:
```powershell
cd "C:\Users\sunka\OneDrive\Desktop\nrml vlsi project"
```

### VCD File Not Generated
**Solution**: Check that `wave/` directory exists:
```powershell
mkdir wave
```

### Permission Denied on Script
**Solution**: Enable script execution in PowerShell:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## File Structure After Compilation

```
project/
├── src/                    (Verilog modules)
│   ├── alu_4bit.v
│   ├── mux4to1.v
│   └── counter3.v
├── tb/                     (Enhanced testbenches)
│   ├── alu_4bit_tb.v      (21 test vectors)
│   ├── mux4to1_tb.v       (10 test cases)
│   └── counter3_tb.v      (Multi-phase test)
├── build/                  (Generated .vvp files)
│   ├── alu_4bit.vvp
│   ├── mux4to1.vvp
│   └── counter3.vvp
├── wave/                   (Generated VCD files)
│   ├── alu_4bit.vcd
│   ├── mux4to1.vcd
│   └── counter3.vcd
└── scripts/
    └── run_iverilog.ps1    (Automation script)
```

---

## Testing Coverage

After installation, your simulations will include:

### ALU (21 test vectors)
- Addition (with/without carry)
- Subtraction (with borrow)
- Logical operations (AND, OR, XOR, XNOR, NOR, PASS)
- Flag testing (zero, carry out)

### MUX (10 test cases)
- All selector combinations (00, 01, 10, 11)
- Various input patterns
- Edge cases and rapid changes

### Counter (Multi-phase)
- Reset behavior
- Counting sequence
- Enable/disable control
- Reset during operation

All results generate VCD files viewable in:
- GTKWave (graphical waveform viewer)
- HTML waveform viewer (site/waveforms.html)

---

## Integration with Project

The enhanced testbenches are Icarus-Verilog compatible and will:
1. Generate accurate waveforms matching Python simulator results
2. Produce industry-standard VCD files
3. Work with both GTKWave and the HTML viewer
4. Provide comprehensive test coverage

No Python environment needed once Icarus Verilog is installed!

---

## Next Steps

1. **Install Icarus Verilog** (choose one method above)
2. **Verify installation**: `iverilog -version`
3. **Run simulations**: `.\scripts\run_iverilog.ps1`
4. **View results**: 
   - Option A: `gtkwave wave/alu_4bit.vcd`
   - Option B: `start site/waveforms.html`

---

## Support

For issues:
- Check iverilog documentation: http://iverilog.icarus.com/
- GitHub issues: https://github.com/steveicarus/iverilog/issues
- Verify all paths use forward slashes or escaped backslashes in PowerShell
