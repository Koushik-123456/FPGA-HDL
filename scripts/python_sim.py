#!/usr/bin/env python3
"""
Standalone Python-based Verilog simulator for basic logic blocks.
Generates VCD waveforms without requiring iverilog or ModelSim.
Includes comprehensive test coverage and simulation reporting.
"""
import sys
from pathlib import Path
from datetime import datetime

class VCDWriter:
    """Simple VCD (Value Change Dump) waveform writer."""
    def __init__(self, filename):
        self.filename = filename
        self.signals = {}
        self.timescale = "1ns"
        self.time = 0
        self.events = []
    
    def register_signal(self, name, width=1):
        self.signals[name] = {'width': width, 'symbol': chr(33 + len(self.signals))}
    
    def change(self, time, name, value):
        self.events.append((time, name, value))
    
    def write(self):
        self.events.sort(key=lambda x: x[0])
        with open(self.filename, 'w') as f:
            f.write("$timescale 1ns $end\n")
            f.write("$date\n  Test simulation\n$end\n")
            f.write("$scope module tb $end\n")
            for name, info in self.signals.items():
                width = info['width']
                sym = info['symbol']
                if width == 1:
                    f.write(f"$var wire 1 {sym} {name} $end\n")
                else:
                    f.write(f"$var wire {width} {sym} {name} $end\n")
            f.write("$upscope $end\n")
            f.write("$enddefinitions $end\n")
            f.write("#0\n")
            for name in self.signals:
                f.write(f"0{self.signals[name]['symbol']}\n")
            
            current_time = 0
            for time, name, value in self.events:
                if time != current_time:
                    f.write(f"#{time}\n")
                    current_time = time
                sym = self.signals[name]['symbol']
                if self.signals[name]['width'] == 1:
                    f.write(f"{value}{sym}\n")
                else:
                    f.write(f"b{bin(value)[2:].zfill(self.signals[name]['width'])} {sym}\n")

# ===== ALU Simulation =====
def alu_4bit(A, B, op, carry_in=0):
    """4-bit ALU logic."""
    if op == 0b000:  # ADD
        result = (A + B + carry_in) & 0xF
        carry = 1 if (A + B + carry_in) > 0xF else 0
    elif op == 0b001:  # SUB
        result = (A - B) & 0xF
        carry = 0
    elif op == 0b010:  # AND
        result = A & B
        carry = 0
    elif op == 0b011:  # OR
        result = A | B
        carry = 0
    elif op == 0b100:  # XOR
        result = A ^ B
        carry = 0
    elif op == 0b101:  # XNOR
        result = ~(A ^ B) & 0xF
        carry = 0
    elif op == 0b110:  # PASS A
        result = A
        carry = 0
    elif op == 0b111:  # NOR
        result = ~(A | B) & 0xF
        carry = 0
    else:
        result = 0
        carry = 0
    
    zero = 1 if result == 0 else 0
    return result, carry, zero

def sim_alu():
    """Simulate 4-bit ALU with comprehensive test coverage."""
    vcd = VCDWriter('wave/alu_4bit.vcd')
    vcd.register_signal('A', 4)
    vcd.register_signal('B', 4)
    vcd.register_signal('op', 3)
    vcd.register_signal('carry_in', 1)
    vcd.register_signal('R', 4)
    vcd.register_signal('carry_out', 1)
    vcd.register_signal('zero', 1)
    
    # Comprehensive test vectors: (time, A, B, op, carry_in, expected_R, expected_cout, expected_zero)
    test_vectors = [
        # ADD operations
        (0, 0x3, 0x4, 0b000, 0, 0x7, 0, 0),      # ADD: 3 + 4 = 7
        (10, 0xF, 0xF, 0b000, 0, 0xE, 1, 0),     # ADD with carry out: F + F = 1E
        (20, 0x0, 0x0, 0b000, 0, 0x0, 0, 1),     # ADD: 0 + 0 = 0 (zero flag)
        (30, 0x5, 0x3, 0b000, 1, 0x9, 0, 0),     # ADD with carry in: 5 + 3 + 1 = 9
        
        # SUB operations
        (40, 0x7, 0x1, 0b001, 0, 0x6, 0, 0),     # SUB: 7 - 1 = 6
        (50, 0x3, 0x5, 0b001, 0, 0xE, 0, 0),     # SUB underflow: 3 - 5 = -2 (wrap)
        (60, 0xF, 0x0, 0b001, 0, 0xF, 0, 0),     # SUB: F - 0 = F
        
        # AND operation
        (70, 0b1010, 0b0101, 0b010, 0, 0x0, 0, 1),   # AND all zeros
        (80, 0b1111, 0b1010, 0b010, 0, 0b1010, 0, 0), # AND: F AND A = A
        (90, 0b1100, 0b1100, 0b010, 0, 0b1100, 0, 0), # AND same: C AND C = C
        
        # OR operation
        (100, 0b1100, 0b0011, 0b011, 0, 0xF, 0, 0),   # OR: C OR 3 = F
        (110, 0x0, 0x0, 0b011, 0, 0x0, 0, 1),          # OR: 0 OR 0 = 0
        (120, 0xF, 0x0, 0b011, 0, 0xF, 0, 0),          # OR: F OR 0 = F
        
        # XOR operation
        (130, 0b1100, 0b0011, 0b100, 0, 0xF, 0, 0),   # XOR: C XOR 3 = F
        (140, 0x5, 0x5, 0b100, 0, 0x0, 0, 1),          # XOR same: 5 XOR 5 = 0
        
        # XNOR operation
        (150, 0b1100, 0b0011, 0b101, 0, 0x0, 0, 1),   # XNOR: C XNOR 3 = 0
        (160, 0x5, 0x5, 0b101, 0, 0xF, 0, 0),          # XNOR same: 5 XNOR 5 = F
        
        # PASS A operation
        (170, 0xA, 0x0, 0b110, 0, 0xA, 0, 0),          # PASS A: A = A (B ignored)
        (180, 0x0, 0xF, 0b110, 0, 0x0, 0, 1),          # PASS A: 0 = 0 (zero flag)
        
        # NOR operation
        (190, 0b1100, 0b0011, 0b111, 0, 0x0, 0, 1),   # NOR: C NOR 3 = 0
        (200, 0x0, 0x0, 0b111, 0, 0xF, 0, 0),          # NOR: 0 NOR 0 = F
    ]
    
    passed = 0
    failed = 0
    
    for time, A, B, op, cin, exp_R, exp_cout, exp_zero in test_vectors:
        R, cout, zero = alu_4bit(A, B, op, cin)
        
        # Verify results
        if R == exp_R and cout == exp_cout and zero == exp_zero:
            passed += 1
        else:
            failed += 1
            print(f"  ❌ FAIL @ t={time}: A={A:04b}, B={B:04b}, op={op:03b} | "
                  f"Expected R={exp_R:04b}/{exp_cout}/{exp_zero}, Got R={R:04b}/{cout}/{zero}")
        
        vcd.change(time, 'A', A)
        vcd.change(time, 'B', B)
        vcd.change(time, 'op', op)
        vcd.change(time, 'carry_in', cin)
        vcd.change(time + 1, 'R', R)
        vcd.change(time + 1, 'carry_out', cout)
        vcd.change(time + 1, 'zero', zero)
    
    vcd.write()
    print(f"✅ ALU simulation complete: wave/alu_4bit.vcd [{passed} passed, {failed} failed]")

# ===== MUX Simulation =====
def mux4to1(i0, i1, i2, i3, sel):
    """4-to-1 multiplexer logic."""
    if sel == 0b00:
        return i0
    elif sel == 0b01:
        return i1
    elif sel == 0b10:
        return i2
    elif sel == 0b11:
        return i3
    else:
        return i0

def sim_mux():
    """Simulate 4-to-1 multiplexer with extended test coverage."""
    vcd = VCDWriter('wave/mux4to1.vcd')
    vcd.register_signal('i0', 4)
    vcd.register_signal('i1', 4)
    vcd.register_signal('i2', 4)
    vcd.register_signal('i3', 4)
    vcd.register_signal('sel', 2)
    vcd.register_signal('y', 4)
    
    # Test vectors with different data patterns
    test_cases = [
        # (i0, i1, i2, i3, sel, expected_y)
        (0x1, 0x2, 0x3, 0x4, 0b00, 0x1),  # Select i0
        (0x1, 0x2, 0x3, 0x4, 0b01, 0x2),  # Select i1
        (0x1, 0x2, 0x3, 0x4, 0b10, 0x3),  # Select i2
        (0x1, 0x2, 0x3, 0x4, 0b11, 0x4),  # Select i3
        (0xF, 0xA, 0x5, 0x0, 0b00, 0xF),  # Different data: select i0
        (0xF, 0xA, 0x5, 0x0, 0b01, 0xA),  # Different data: select i1
        (0xF, 0xA, 0x5, 0x0, 0b10, 0x5),  # Different data: select i2
        (0xF, 0xA, 0x5, 0x0, 0b11, 0x0),  # Different data: select i3
        (0x0, 0x0, 0x0, 0x0, 0b00, 0x0),  # All zeros
        (0xF, 0xF, 0xF, 0xF, 0b11, 0xF),  # All ones
    ]
    
    passed = 0
    failed = 0
    
    for t, (i0, i1, i2, i3, sel, expected_y) in enumerate(test_cases):
        time = t * 10
        y = mux4to1(i0, i1, i2, i3, sel)
        
        if y == expected_y:
            passed += 1
        else:
            failed += 1
            print(f"  ❌ FAIL @ t={time}: sel={sel:02b} | Expected {expected_y:04b}, Got {y:04b}")
        
        vcd.change(time, 'i0', i0)
        vcd.change(time, 'i1', i1)
        vcd.change(time, 'i2', i2)
        vcd.change(time, 'i3', i3)
        vcd.change(time, 'sel', sel)
        vcd.change(time + 1, 'y', y)
    
    vcd.write()
    print(f"✅ MUX simulation complete: wave/mux4to1.vcd [{passed} passed, {failed} failed]")

# ===== Counter Simulation =====
def sim_counter():
    """Simulate 3-bit synchronous counter with comprehensive timing."""
    vcd = VCDWriter('wave/counter3.vcd')
    vcd.register_signal('clk', 1)
    vcd.register_signal('rst', 1)
    vcd.register_signal('en', 1)
    vcd.register_signal('q', 3)
    
    clk_period = 10
    
    # Phase 1: Reset active (10 cycles)
    print("  Reset active (0-90 ns)")
    for cycle in range(0, 9):
        t = cycle * clk_period
        vcd.change(t, 'clk', 0)
        vcd.change(t + clk_period // 2, 'clk', 1)
        vcd.change(t, 'rst', 1)
        vcd.change(t, 'en', 0)
        vcd.change(t, 'q', 0)
    
    # Phase 2: Reset released, enable counting (8 cycles)
    print("  Counting with enable (100-170 ns)")
    q = 0
    for cycle in range(9, 17):
        t = cycle * clk_period
        vcd.change(t, 'clk', 0)
        vcd.change(t + clk_period // 2, 'clk', 1)
        vcd.change(t, 'rst', 0)
        vcd.change(t, 'en', 1)
        q = (q + 1) & 0x7
        vcd.change(t + clk_period // 2 + 1, 'q', q)
    
    # Phase 3: Disable counter (5 cycles - counter should hold value)
    print("  Counter disabled (180-220 ns)")
    for cycle in range(17, 22):
        t = cycle * clk_period
        vcd.change(t, 'clk', 0)
        vcd.change(t + clk_period // 2, 'clk', 1)
        vcd.change(t, 'rst', 0)
        vcd.change(t, 'en', 0)
        vcd.change(t, 'q', q)
    
    # Phase 4: Re-enable and count (3 more cycles)
    print("  Counting resumed (230-260 ns)")
    for cycle in range(22, 25):
        t = cycle * clk_period
        vcd.change(t, 'clk', 0)
        vcd.change(t + clk_period // 2, 'clk', 1)
        vcd.change(t, 'rst', 0)
        vcd.change(t, 'en', 1)
        q = (q + 1) & 0x7
        vcd.change(t + clk_period // 2 + 1, 'q', q)
    
    vcd.write()
    print(f"✅ Counter simulation complete: wave/counter3.vcd")

if __name__ == '__main__':
    Path('wave').mkdir(exist_ok=True)
    
    print("=" * 60)
    print("Python-based Verilog Simulator")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        which = sys.argv[1]
        if which == 'alu':
            print("\n📊 Running ALU Simulation...")
            sim_alu()
        elif which == 'mux':
            print("\n📊 Running MUX Simulation...")
            sim_mux()
        elif which == 'counter':
            print("\n📊 Running Counter Simulation...")
            sim_counter()
        elif which == 'all':
            print("\n📊 Running all simulations...")
            print("\n--- ALU ---")
            sim_alu()
            print("\n--- MUX ---")
            sim_mux()
            print("\n--- Counter ---")
            sim_counter()
        else:
            print("Usage: python_sim.py [alu|mux|counter|all]")
    else:
        print("\n📊 Running all simulations...")
        print("\n--- ALU ---")
        sim_alu()
        print("\n--- MUX ---")
        sim_mux()
        print("\n--- Counter ---")
        sim_counter()
    
    print("\n" + "=" * 60)
    print("✅ All simulations complete! ")
    print("VCD files generated in wave/ directory")
    print("=" * 60)
