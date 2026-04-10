`timescale 1ns/1ps

module tb_alu_4bit();

reg [3:0] A, B;
reg [2:0] op;
reg cin;
wire [3:0] R;
wire cout;
wire zero;

// Instantiate the ALU
alu_4bit uut (
    .A(A),
    .B(B),
    .op(op),
    .carry_in(cin),
    .R(R),
    .carry_out(cout),
    .zero(zero)
);

// Test vectors matching the Python simulator
initial begin
    $dumpfile("wave/alu_4bit.vcd");
    $dumpvars(0, tb_alu_4bit);
    
    // Test 1: ADD 3 + 4 = 7
    A = 4'd3; B = 4'd4; cin = 0; op = 3'b000; #10;
    
    // Test 2: ADD 15 + 15 = 30 (with carry)
    A = 4'hF; B = 4'hF; cin = 0; op = 3'b000; #10;
    
    // Test 3: ADD with carry input
    A = 4'hF; B = 4'h0; cin = 1; op = 3'b000; #10;
    
    // Test 4: SUB 7 - 1 = 6
    A = 4'd7; B = 4'd1; cin = 0; op = 3'b001; #10;
    
    // Test 5: SUB 0 - 1 = -1 (15)
    A = 4'd0; B = 4'd1; cin = 0; op = 3'b001; #10;
    
    // Test 6: SUB with borrow
    A = 4'd5; B = 4'd7; cin = 0; op = 3'b001; #10;
    
    // Test 7: AND 0xA & 0x5 = 0x0
    A = 4'hA; B = 4'h5; cin = 0; op = 3'b010; #10;
    
    // Test 8: AND 0xF & 0xC = 0xC
    A = 4'hF; B = 4'hC; cin = 0; op = 3'b010; #10;
    
    // Test 9: OR 0xC | 0x3 = 0xF
    A = 4'hC; B = 4'h3; cin = 0; op = 3'b011; #10;
    
    // Test 10: OR 0x0 | 0x0 = 0x0
    A = 4'h0; B = 4'h0; cin = 0; op = 3'b011; #10;
    
    // Test 11: XOR 0xF ^ 0xF = 0x0
    A = 4'hF; B = 4'hF; cin = 0; op = 3'b100; #10;
    
    // Test 12: XOR 0x5 ^ 0xA = 0xF
    A = 4'h5; B = 4'hA; cin = 0; op = 3'b100; #10;
    
    // Test 13: XNOR 0xA ^ 0x5 = 0x0 inverted
    A = 4'hA; B = 4'h5; cin = 0; op = 3'b101; #10;
    
    // Test 14: XNOR (all ones)
    A = 4'hF; B = 4'hF; cin = 0; op = 3'b101; #10;
    
    // Test 15: PASS A
    A = 4'h7; B = 4'hX; cin = 0; op = 3'b110; #10;
    
    // Test 16: PASS B
    A = 4'hX; B = 4'h9; cin = 0; op = 3'b110; #10;
    
    // Test 17: NOR 0xC NOR 0x3 = 0x0
    A = 4'hC; B = 4'h3; cin = 0; op = 3'b111; #10;
    
    // Test 18: NOR (all ones)
    A = 4'hF; B = 4'hF; cin = 0; op = 3'b111; #10;
    
    // Test 19: Zero flag test (result = 0)
    A = 4'h5; B = 4'h5; cin = 0; op = 3'b001; #10; // 5 - 5 = 0
    
    // Test 20: Carry out on ADD
    A = 4'hE; B = 4'h3; cin = 0; op = 3'b000; #10; // 14 + 3 = 17 (carry)
    
    // Test 21: Complex operation
    A = 4'h8; B = 4'h4; cin = 1; op = 3'b000; #10; // 8 + 4 + 1 = 13
    
    $display("ALU simulation complete - 21 test vectors executed");
    $finish;
end

endmodule
