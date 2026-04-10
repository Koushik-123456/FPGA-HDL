# Schematic-level verification notes

This file describes how to reproduce the same logic using schematic primitives (AND, OR, XOR, multiplexers, counters) and compare behavior with the HDL simulation.

Suggested flow:

1) Open your FPGA tool (Vivado/Quartus) and create a new schematic or block design.
2) Implement the blocks using primitives:
   - ALU: use add/subtract, logic gates for AND/OR/XOR, and multiplexers to select the output based on `op`.
   - MUX: use a 4-to-1 multiplexer primitive; parameterize bit-width as needed.
   - Counter: use a 3-bit register bank with synchronous increment and reset.
3) Create the same stimulus as in the testbenches and run functional simulation.
4) Export waveforms from the schematic simulation (VCD or native waveform) and open with GTKWave or ModelSim.
5) Compare key signals (outputs and status flags) across the HDL and schematic simulations to ensure they match.

Tips
- Keep signal names consistent between HDL and schematic for easier VCD correlation.
- For combinational blocks ensure propagation is zero-delay in functional sims when comparing behavior; for timing checks use post-route simulation.
