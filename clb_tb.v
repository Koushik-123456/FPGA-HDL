`timescale 1ns / 1ps

module clb_tb;

// Testbench signals
reg a, b, sel;
reg [3:0] in4;
reg [1:0] sel4;
reg [2:0] dec_in;
reg cin;
reg clk, reset;

wire mux2_out;
wire mux4_out;
wire [7:0] dec_out;
wire sum, cout;
wire q;
wire [3:0] count;

integer i;

// Instantiate the top module
clb_top dut (
    .a(a), .b(b), .sel(sel),
    .in4(in4), .sel4(sel4),
    .dec_in(dec_in), .cin(cin),
    .clk(clk), .reset(reset),
    .mux2_out(mux2_out), .mux4_out(mux4_out),
    .dec_out(dec_out), .sum(sum), .cout(cout),
    .q(q), .count(count)
);

// Clock generation
always #5 clk = ~clk;

initial
begin
    $dumpfile("clb_sim.vcd");
    $dumpvars(0, clb_tb);
    
    // Initialize
    clk = 0;
    reset = 1;
    a = 0;
    b = 0;
    sel = 0;
    in4 = 4'b0000;
    sel4 = 2'b00;
    dec_in = 3'b000;
    cin = 0;
    
    #10 reset = 0;
    
    // Test 2:1 MUX
    $display("\n===== Testing 2:1 MUX =====");
    a = 1'b0; b = 1'b1; sel = 1'b0;
    #10 $display("a=%b, b=%b, sel=%b => mux2_out=%b (expected 0)", a, b, sel, mux2_out);
    
    sel = 1'b1;
    #10 $display("a=%b, b=%b, sel=%b => mux2_out=%b (expected 1)", a, b, sel, mux2_out);
    
    // Test 4:1 MUX
    $display("\n===== Testing 4:1 MUX =====");
    in4 = 4'b1010;
    for (i = 0; i < 4; i = i + 1) begin
        sel4 = i;
        #10 $display("sel4=%d => mux4_out=%b", i, mux4_out);
    end
    
    // Test 3:8 DECODER
    $display("\n===== Testing 3:8 DECODER =====");
    for (i = 0; i < 8; i = i + 1) begin
        dec_in = i;
        #10 $display("dec_in=%d => dec_out=%08b", i, dec_out);
    end
    
    // Test Full Adder
    $display("\n===== Testing FULL ADDER =====");
    a = 1'b0; b = 1'b0; cin = 1'b0;
    #10 $display("a=%b, b=%b, cin=%b => sum=%b, cout=%b", a, b, cin, sum, cout);
    
    a = 1'b1; b = 1'b1; cin = 1'b1;
    #10 $display("a=%b, b=%b, cin=%b => sum=%b, cout=%b", a, b, cin, sum, cout);
    
    // Test D Flip-Flop
    $display("\n===== Testing D FLIP-FLOP =====");
    a = 1'b1;
    #10 $display("Clock pulse: d=%b => q=%b", a, q);
    a = 1'b0;
    #10 $display("Clock pulse: d=%b => q=%b", a, q);
    a = 1'b1;
    #10 $display("Clock pulse: d=%b => q=%b", a, q);
    
    // Test 4-BIT COUNTER
    $display("\n===== Testing 4-BIT COUNTER =====");
    reset = 1;
    #20 reset = 0;
    for (i = 0; i < 10; i = i + 1) begin
        #10 $display("Clock pulse %d: count=%d", i, count);
    end
    
    // Test reset
    reset = 1;
    #10 $display("After reset: count=%d", count);
    
    #20 $finish;
end

endmodule
