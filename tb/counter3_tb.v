`timescale 1ns/1ps

module tb_counter3();

reg clk;
reg rst;
reg en;
wire [2:0] q;

// Instantiate the counter
counter3 uut (
    .clk(clk),
    .rst(rst),
    .en(en),
    .q(q)
);

// Clock generation
initial begin
    clk = 0;
    forever #5 clk = ~clk;  // 10ns period
end

// Test procedure
initial begin
    $dumpfile("wave/counter3.vcd");
    $dumpvars(0, tb_counter3);
    
    // Phase 1: Reset
    rst = 1;
    en = 0;
    #10;
    
    // Phase 2: Reset release, counter disabled
    rst = 0;
    en = 0;
    #20;
    
    // Phase 3: Enable counter - count up
    rst = 0;
    en = 1;
    #70;  // 7 clock cycles to see full count
    
    // Phase 4: Disable counter
    en = 0;
    #20;
    
    // Phase 5: Re-enable counter
    en = 1;
    #30;
    
    // Phase 6: Reset during counting
    rst = 1;
    #10;
    rst = 0;
    en = 1;
    #20;
    
    // Phase 7: Final counting phase
    en = 1;
    #50;
    
    $display("Counter simulation complete - all test phases executed");
    $finish;
end

endmodule
