# VLSI CLB (Configurable Logic Block) Design

## Overview
This project contains digital logic building blocks designed for VLSI implementation using Vivado.

## Modules

### 1. **2:1 Multiplexer** (`mux2to1`)
- Inputs: `a`, `b`, `sel`
- Output: `y`
- Selects between two 1-bit inputs

### 2. **4:1 Multiplexer** (`mux4to1`)
- Inputs: `in[3:0]` (4-bit), `sel[1:0]` (2-bit selector)
- Output: `y`
- Selects one of four inputs

### 3. **3:8 Decoder** (`decoder3to8`)
- Input: `a[2:0]` (3-bit address)
- Output: `y[7:0]` (8-bit one-hot encoded)
- Decodes 3-bit input to 8 active lines

### 4. **Full Adder** (`full_adder`)
- Inputs: `a`, `b`, `cin`
- Outputs: `sum`, `cout`
- Standard 1-bit full adder

### 5. **D Flip-Flop** (`d_ff`)
- Inputs: `clk`, `d`
- Output: `q`
- Captures data on rising clock edge

### 6. **4-Bit Counter** (`counter4bit`)
- Inputs: `clk`, `reset`
- Output: `count[3:0]`
- Increments on each clock cycle, resets when reset is asserted

### 7. **Top Module** (`clb_top`)
- Hierarchical instantiation of all modules above
- Complete testbench provided for validation

## File Structure
```
├── clb_design.v      # Main design file with all modules
├── clb_tb.v          # Testbench with comprehensive test cases
├── .gitignore        # Git ignore rules for Vivado projects
└── README.md         # This file
```

## Simulation Results

To view simulation results:
1. Open the Vivado project
2. Run behavioral simulation
3. Check the waveforms directory for `.wdb` and `.vcd` files
4. Review the simulation log from Vivado console

## Quick Simulation Commands

If using iverilog:
```bash
iverilog -o clb_sim clb_design.v clb_tb.v
vvp clb_sim
```

## Tools Used
- **Vivado Design Suite** (for synthesis and implementation)
- **iverilog** (optional, for open-source simulation)

## Version History
- **v1.0**: Initial design with basic modules and testbench

## Author
VLSI Design Team

## Notes
- All modules use synchronous design principles
- Testbench includes automated test cases for all modules
- Waveform captures are saved in Vivado simulation outputs
