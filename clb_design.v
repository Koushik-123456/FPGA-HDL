//================= 2:1 MUX =================
module mux2to1(input a, input b, input sel, output y);
assign y = sel ? b : a;
endmodule

//================= 4:1 MUX =================
module mux4to1(input [3:0] in, input [1:0] sel, output y);
assign y = (sel == 2'b00) ? in[0] :
           (sel == 2'b01) ? in[1] :
           (sel == 2'b10) ? in[2] : in[3];
endmodule

//================= 3:8 DECODER =================
module decoder3to8(input [2:0] a, output [7:0] y);
assign y = 8'b00000001 << a;
endmodule

//================= FULL ADDER =================
module full_adder(input a, input b, input cin, output sum, output cout);
assign sum  = a ^ b ^ cin;
assign cout = (a & b) | (b & cin) | (a & cin);
endmodule

//================= D FLIP-FLOP =================
module d_ff(input clk, input d, output reg q);
always @(posedge clk)
    q <= d;
endmodule

//================= 4-BIT COUNTER =================
module counter4bit(input clk, input reset, output reg [3:0] count);
always @(posedge clk or posedge reset)
begin
    if (reset)
        count <= 4'b0000;
    else
        count <= count + 1;
end
endmodule

//================= TOP MODULE =================
module clb_top(
    input a, b, sel,
    input [3:0] in4,
    input [1:0] sel4,
    input [2:0] dec_in,
    input cin,
    input clk, reset,
    output mux2_out,
    output mux4_out,
    output [7:0] dec_out,
    output sum, cout,
    output q,
    output [3:0] count
);

// Instantiations
mux2to1 m1 (.a(a), .b(b), .sel(sel), .y(mux2_out));
mux4to1 m2 (.in(in4), .sel(sel4), .y(mux4_out));
decoder3to8 d1 (.a(dec_in), .y(dec_out));
full_adder fa1 (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));
d_ff dff1 (.clk(clk), .d(a), .q(q));
counter4bit c1 (.clk(clk), .reset(reset), .count(count));

endmodule
