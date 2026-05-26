# FPGA HDL Verification Project

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Repo Size](https://img.shields.io/github/repo-size/Koushik-123456/FPGA-HDL)](https://github.com/Koushik-123456/FPGA-HDL)

A practical FPGA HDL verification repository demonstrating Verilog logic blocks, simulation testbenches, and a Vivado example flow.

## Overview

This repository includes a configurable logic block (CLB) design with supporting modules and verification infrastructure. It is designed for learning, demonstration, and FPGA verification workflows.

### Included examples
- 4-bit ALU (`src/alu_4bit.v`)
- 4-to-1 multiplexer (`src/mux4to1.v`) with parameterized width
- 3-bit synchronous counter (`src/counter3.v`)
- Top-level CLB design and testbench (`clb_design.v`, `clb_tb.v`)

## Repository Structure

- `clb_design.v` — top-level CLB RTL
- `clb_tb.v` — primary design verification testbench
- `src/` — core Verilog modules
- `tb/` — module-level testbenches
- `scripts/` — automation and simulation helper scripts
- `vivado/` — Vivado TCL example project flow
- `docs/` — documentation and schematic notes
- `simulations/` — generated logs and waveform outputs
- `bitstream/` — generated FPGA bitstream
- `reports/` — synthesis and implementation reports

## Quick Start

### Prerequisites
- Verilog simulator (Icarus Verilog, ModelSim, Vivado)
- GTKWave for waveform viewing (optional)
- Python 3 for local documentation preview

### Run simulation on Windows

```powershell
cd "C:\Users\sunka\OneDrive\Desktop\vlsi vivado"
.\scripts\run_sim.ps1 alu
.\scripts\run_sim.ps1 mux
.\scripts\run_sim.ps1 counter
```

### Run simulation with Icarus Verilog

```bash
make sim_alu
make sim_mux
make sim_counter
```

### View generated waveforms

Waveform output files are available in:

- `simulations/waveforms/`

Open the VCD files in GTKWave or another waveform viewer.

## Vivado Example Flow

Use the provided Vivado script to create a project and run simulation.

```bash
vivado -mode batch -source vivado/run_sim.tcl
```

Update the FPGA device part in `vivado/run_sim.tcl` before running if required.

## Documentation

See `docs/` for additional design notes, RTL schematics, and verification guidance.

## Notes

- `requirements.txt` is intentionally minimal and documents that no external dependencies are required for the core Verilog flow.
- Generated directories such as `bitstream/`, `reports/`, `simulations/`, and `site/` can be removed for a cleaner source-only repository.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
