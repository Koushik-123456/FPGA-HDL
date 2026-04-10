`timescale 1ns/1ps

module tb_mux4to1();

reg [3:0] i0, i1, i2, i3;
reg [1:0] sel;
wire [3:0] y;

// Instantiate the MUX
mux4to1 #(.WIDTH(4)) uut (
    .i0(i0),
    .i1(i1),
    .i2(i2),
    .i3(i3),
    .sel(sel),
    .y(y)
);

// Test vectors matching the Python simulator
initial begin
    $dumpfile("wave/mux4to1.vcd");
    $dumpvars(0, tb_mux4to1);
    
    // Test 1: Select i0 (sel = 00)
    i0 = 4'hA; i1 = 4'hB; i2 = 4'hC; i3 = 4'hD;
    sel = 2'b00; #10;
    
    // Test 2: Select i1 (sel = 01)
    i0 = 4'h1; i1 = 4'h2; i2 = 4'h3; i3 = 4'h4;
    sel = 2'b01; #10;
    
    // Test 3: Select i2 (sel = 10)
    i0 = 4'h5; i1 = 4'h6; i2 = 4'h7; i3 = 4'h8;
    sel = 2'b10; #10;
    
    // Test 4: Select i3 (sel = 11)
    i0 = 4'h9; i1 = 4'hA; i2 = 4'hB; i3 = 4'hC;
    sel = 2'b11; #10;
    
    // Test 5: All inputs 0xFF
    i0 = 4'hF; i1 = 4'hF; i2 = 4'hF; i3 = 4'hF;
    sel = 2'b00; #10;
    sel = 2'b01; #10;
    sel = 2'b10; #10;
    sel = 2'b11; #10;
    
    // Test 6: All inputs 0x00
    i0 = 4'h0; i1 = 4'h0; i2 = 4'h0; i3 = 4'h0;
    sel = 2'b00; #10;
    sel = 2'b01; #10;
    sel = 2'b10; #10;
    sel = 2'b11; #10;
    
    // Test 7: Pattern test - alternating bits
    i0 = 4'hA; i1 = 4'h5; i2 = 4'hA; i3 = 4'h5;
    sel = 2'b00; #10;
    sel = 2'b01; #10;
    sel = 2'b10; #10;
    sel = 2'b11; #10;
    
    // Test 8: Rapid selection changes
    i0 = 4'h7; i1 = 4'h8; i2 = 4'h9; i3 = 4'hE;
    sel = 2'b00; #5;
    sel = 2'b01; #5;
    sel = 2'b10; #5;
    sel = 2'b11; #5;
    
    // Test 9: Edge case - single bit set
    i0 = 4'h1; i1 = 4'h2; i2 = 4'h4; i3 = 4'h8;
    sel = 2'b00; #10;
    sel = 2'b01; #10;
    sel = 2'b10; #10;
    sel = 2'b11; #10;
    
    // Test 10: Input change without sel change
    sel = 2'b00; #10;
    i0 = 4'h3; #10;
    i0 = 4'h6; #10;
    i0 = 4'h9; #10;
    
    $display("MUX simulation complete - 10 test cases executed");
    $finish;
end

endmodule
