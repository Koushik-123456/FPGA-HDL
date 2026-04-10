IVERILOG = iverilog
VVP = vvp
GTKWAVE = gtkwave

all: sim_all

sim_alu:
	$(IVERILOG) -o wave/alu_4bit.vvp tb/alu_4bit_tb.v src/alu_4bit.v
	$(VVP) wave/alu_4bit.vvp

sim_mux:
	$(IVERILOG) -o wave/mux4to1.vvp tb/mux4to1_tb.v src/mux4to1.v
	$(VVP) wave/mux4to1.vvp

sim_counter:
	$(IVERILOG) -o wave/counter3.vvp tb/counter3_tb.v src/counter3.v
	$(VVP) wave/counter3.vvp

sim_all: sim_alu sim_mux sim_counter

clean:
	rm -rf wave/*.vcd wave/*.vvp
