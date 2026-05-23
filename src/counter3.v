// 3-bit synchronous up-counter with enable and synchronous reset
module counter3(
    input clk,
    input rst, // synchronous active-high
    input en,
    output reg [2:0] q
);

always @(posedge clk) begin
    if (rst) q <= 3'b000;
    else if (en) q <= q + 1'b1;
end

endmodule
