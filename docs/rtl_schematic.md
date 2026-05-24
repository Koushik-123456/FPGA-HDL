# RTL Schematic Overview

This file provides a high-level RTL schematic description for the project modules.

## Top-level RTL structure

- `clb_design.v` is the top-level Verilog entry point for the configurable logic block (CLB) design.
- The design uses the following submodules:
  - `src/alu_4bit.v` — 4-bit arithmetic logic unit with add/sub, logic operations, and flag outputs.
  - `src/mux4to1.v` — 4-to-1 multiplexer with parameterizable data width.
  - `src/counter3.v` — 3-bit synchronous counter with reset and enable.

## Module connections

### ALU (`alu_4bit`)
- Inputs:
  - `a[3:0]`
  - `b[3:0]`
  - `op[1:0]`
- Outputs:
  - `out[3:0]`
  - `zero`
  - `carry`
  - `overflow`

### MUX (`mux4to1`)
- Inputs:
  - `sel[1:0]`
  - `in0[3:0]`
  - `in1[3:0]`
  - `in2[3:0]`
  - `in3[3:0]`
- Output:
  - `out[3:0]`

### Counter (`counter3`)
- Inputs:
  - `clk`
  - `rst`
  - `en`
- Output:
  - `count[2:0]`

## RTL schematic block diagram

```text
      +-----------------+
      |    clb_design    |
      |                 |
      | +-------------+ |
      | |  alu_4bit   | |
      | |             | |
 a[3:0]-->| a         | |
 b[3:0]-->| b         | |
op[1:0]-->| op        | |
      | | out[3:0]   | |
      | +-------------+ |
      |                 |
      | +-------------+ |
      | | mux4to1     | |
      | |             | |
      | | sel[1:0]   | |
      | | in0..in3   | |
      | | out[3:0]   | |
      | +-------------+ |
      |                 |
      | +-------------+ |
      | | counter3    | |
 clk --->| clk       | |
 rst --->| rst       | |
 en --->| en        | |
      | | count[2:0] | |
      | +-------------+ |
      +-----------------+
```

## Usage

- Open this file in a text editor or use it as a reference when creating a graphical schematic in Vivado or Quartus.
- This is a lightweight RTL schematic asset for repository tracking and documentation.
