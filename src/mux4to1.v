// Parameterizable 4-to-1 multiplexer
module mux4to1 #(
    parameter WIDTH = 1
)(
    input  [WIDTH-1:0] i0,
    input  [WIDTH-1:0] i1,
    input  [WIDTH-1:0] i2,
    input  [WIDTH-1:0] i3,
    input  [1:0] sel,
    output reg [WIDTH-1:0] y
);

always @* begin
    case (sel)
        2'b00: y = i0;
        2'b01: y = i1;
        2'b10: y = i2;
        2'b11: y = i3;
        default: y = i0;
    endcase
end

endmodule
