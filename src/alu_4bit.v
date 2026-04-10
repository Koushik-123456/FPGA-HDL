// 4-bit ALU
module alu_4bit(
    input [3:0] A,
    input [3:0] B,
    input [2:0] op, // operation select
    input carry_in,
    output reg [3:0] R,
    output reg carry_out,
    output zero
);

always @* begin
    carry_out = 0;
    case (op)
        3'b000: {carry_out, R} = A + B + carry_in; // ADD
        3'b001: {carry_out, R} = ({1'b0, A} - {1'b0, B}); // SUB
        3'b010: R = A & B; // AND
        3'b011: R = A | B; // OR
        3'b100: R = A ^ B; // XOR
        3'b101: R = ~(A ^ B); // XNOR
        3'b110: R = A; // PASS A
        3'b111: R = ~(A | B); // NOR
        default: R = 4'b0000;
    endcase
end

assign zero = (R == 4'b0000);

endmodule
