# FPGA HDL Verification Project

This project provides Verilog implementations and testbenches for common FPGA logic blocks and a simple simulation workflow.

Included examples:
- 4-bit ALU ([src/alu_4bit.v](src/alu_4bit.v))
- 4-to-1 multiplexer ([src/mux4to1.v](src/mux4to1.v)) — parameterizable width
- 3-bit synchronous counter ([src/counter3.v](src/counter3.v))

Project structure
- [src/](src): Verilog sources
- [tb/](tb): Testbenches for simulation
- [scripts/](scripts): helper run scripts (PowerShell)
- [vivado/](vivado): example Vivado TCL for project creation/sim
- [docs/](docs): schematic-level notes

Quickstart (Icarus Verilog + GTKWave)

1) Install Icarus Verilog and GTKWave (or use ModelSim/Vivado)
2) From the project root run (Linux/macOS):

```bash
make sim_alu    # runs ALU testbench (requires iverilog/vvp on PATH)
make sim_mux
make sim_counter
```

On Windows you can use the PowerShell helper:

```powershell
.\scripts\run_sim.ps1 alu
.\scripts\run_sim.ps1 mux
.\scripts\run_sim.ps1 counter
```

Waveforms are written to `wave/*.vcd` by the testbenches and can be opened with GTKWave.

Vivado (optional)

Use the provided TCL script to create a Vivado project and launch simulation (edit target part as needed):

```bash
vivado -mode batch -source vivado/run_sim.tcl
```

Schematic-level verification

See [docs/schematic.md](docs/schematic.md) for guidance on recreating the logic with gates/primitive symbols and comparing waveforms.

Next steps
- Run the provided testbenches with your simulator of choice and inspect `wave/*.vcd` with GTKWave or ModelSim.
- Optionally create an FPGA project in Vivado/Quartus and run timing/implementation flows.
