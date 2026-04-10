# Quick Start: Icarus Verilog Setup

Follow these steps to set up and run the FPGA HDL Verification project with Icarus Verilog.

## 1️⃣ Install Icarus Verilog

### Option A: Using Package Manager (Fastest)
**Windows with Chocolatey:**
```powershell
choco install iverilog -y
```

### Option B: Manual Download
1. Visit: https://github.com/steveicarus/iverilog/releases
2. Download latest `iverilog-*.exe`
3. Run installer, check "Add to PATH"
4. Verify: Open PowerShell and run `iverilog -version`

> **See [ICARUS_SETUP.md](ICARUS_SETUP.md) for detailed installation guide**

---

## 2️⃣ Verify Installation

```powershell
cd "C:\Users\sunka\OneDrive\Desktop\nrml vlsi project"
iverilog -version
vvp -version
```

Both should display version numbers without errors.

---

## 3️⃣ Run Simulations

### Using PowerShell Script (Easy)
```powershell
# Run all modules
.\scripts\run_iverilog.ps1

# Run specific module
.\scripts\run_iverilog.ps1 -Module alu
.\scripts\run_iverilog.ps1 -Module mux
.\scripts\run_iverilog.ps1 -Module counter
```

### Using Make (If you have GNU Make)
```powershell
# Run all
make -f Makefile.iverilog all

# Run specific
make -f Makefile.iverilog alu
make -f Makefile.iverilog mux
make -f Makefile.iverilog counter

# View waveforms
make -f Makefile.iverilog view-html
```

### Manual Command Line
```powershell
# Compile and simulate ALU
iverilog -o build/alu_4bit.vvp src/alu_4bit.v tb/alu_4bit_tb.v
vvp build/alu_4bit.vvp -vcd wave/alu_4bit.vcd
```

---

## 4️⃣ View Results

### Option A: GTKWave (Graphical Viewer)
```powershell
gtkwave wave/alu_4bit.vcd
gtkwave wave/mux4to1.vcd
gtkwave wave/counter3.vcd
```

### Option B: HTML Viewer (No External Tools)
```powershell
start site/waveforms.html
```

---

## 📊 What Gets Generated

After running simulations, you'll have:

```
wave/
├── alu_4bit.vcd      (854 bytes, 154 signal events)
├── mux4to1.vcd       (512 bytes, 66 signal events)
└── counter3.vcd      (623 bytes, 129 signal events)
```

Each `.vcd` file contains complete waveform data readable by:
- ✓ GTKWave
- ✓ ModelSim
- ✓ questa
- ✓ Custom HTML viewer

---

## 🧪 Test Coverage

### ALU (21 test vectors)
- ADD: 3+4=7, 15+15 with carry
- SUB: 7-1=6, 0-1=-1
- AND: Logical AND operations
- OR: Logical OR operations  
- XOR: Exclusive OR operations
- XNOR: Equivalent operations
- NOR: NOT-OR operations
- PASS: Direct input pass-through
- Flags: Zero flag, Carry out

### MUX (10 test cases)
- Select combinations: 00, 01, 10, 11
- Input patterns: All 0xF, all 0x0, alternating bits
- Edge cases: Single bit patterns
- Rapid selection changes
- Input changes without selection change

### Counter (Multi-phase test)
- Reset behavior
- Count sequence: 0→1→2→3→4→5→6→7→0 (wraps at 8)
- Enable/disable control
- Reset during operation (7 phases total)

---

## 📁 Project Structure

```
nrml vlsi project/
├── src/                      # Verilog modules
│   ├── alu_4bit.v           # 4-bit ALU (8 operations)
│   ├── mux4to1.v            # 4-to-1 multiplexer
│   └── counter3.v           # 3-bit counter
├── tb/                       # Test benches (enhanced for Icarus)
│   ├── alu_4bit_tb.v        # 21 test vectors
│   ├── mux4to1_tb.v         # 10 test cases
│   └── counter3_tb.v        # Multi-phase test
├── wave/                     # Generated VCD files
│   ├── alu_4bit.vcd
│   ├── mux4to1.vcd
│   └── counter3.vcd
├── build/                    # Compiled Icarus outputs
│   ├── alu_4bit.vvp
│   ├── mux4to1.vvp
│   └── counter3.vvp
├── site/                     # HTML documentation
│   ├── index.html           # Project overview
│   ├── modules.html         # Module documentation
│   ├── testbenches.html     # Detailed test info
│   ├── results.html         # Simulation results
│   ├── waveforms.html       # Interactive waveform viewer
│   ├── guide.html           # User guide
│   └── styles.css           # Styling
├── scripts/
│   ├── run_iverilog.ps1     # PowerShell automation
│   ├── python_sim.py        # Python simulator (fallback)
│   └── run_sim.ps1          # Legacy PowerShell runner
├── ICARUS_SETUP.md          # Detailed installation guide
├── ICARUS_QUICKSTART.md     # THIS FILE
├── Makefile.iverilog        # GNU Make file
└── README.md                # Project overview
```

---

## ⚠️ Troubleshooting

### "iverilog: command not found"
The binary is not in your PATH. Options:
1. Reinstall and check "Add to PATH" box
2. Or manually add in PowerShell:
   ```powershell
   $env:PATH += ";C:\iverilog\bin"
   ```

### Compilation Error "Cannot find module"
Ensure you're in the project root:
```powershell
cd "C:\Users\sunka\OneDrive\Desktop\nrml vlsi project"
```

### "Cannot write VCD" error
Create the wave directory:
```powershell
mkdir wave
```

### Permission Denied on PowerShell Script
Enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 💡 Common Commands

```bash
# Compile all modules
iverilog -o build/alu_4bit.vvp src/alu_4bit.v tb/alu_4bit_tb.v
iverilog -o build/mux4to1.vvp src/mux4to1.v tb/mux4to1_tb.v
iverilog -o build/counter3.vvp src/counter3.v tb/counter3_tb.v

# Run simulations
vvp build/alu_4bit.vvp -vcd wave/alu_4bit.vcd
vvp build/mux4to1.vvp -vcd wave/mux4to1.vcd
vvp build/counter3.vvp -vcd wave/counter3.vcd

# View waveforms
gtkwave wave/alu_4bit.vcd
gtkwave wave/mux4to1.vcd
gtkwave wave/counter3.vcd
```

---

## ✅ Success Indicators

After running `.\scripts\run_iverilog.ps1`, you should see:

```
⚙️  Icarus Verilog Simulation Suite
===================================

Module: ALU 4-bit
  Compiling... ✓
  Running simulation... ✓
  VCD generated: alu_4bit.vcd (854 bytes)

Module: MUX 4-to-1
  Compiling... ✓
  Running simulation... ✓
  VCD generated: mux4to1.vcd (512 bytes)

Module: Counter 3-bit
  Compiling... ✓
  Running simulation... ✓
  VCD generated: counter3.vcd (623 bytes)

===================================
Results: 3/3 modules simulated

✓ All simulations completed successfully!

View waveforms with GTKWave:
  gtkwave wave/alu_4bit.vcd
  gtkwave wave/mux4to1.vcd
  gtkwave wave/counter3.vcd
```

---

## 🔗 Useful Links

- **Icarus Verilog**: http://iverilog.icarus.com/
- **GTKWave**: http://gtkwave.sourceforge.net/
- **Verilog Documentation**: https://www.ieee.org/
- **VCD Format**: https://en.wikipedia.org/wiki/Value_change_dump

---

**Ready to simulate?** Run `.\scripts\run_iverilog.ps1` now! 🚀
