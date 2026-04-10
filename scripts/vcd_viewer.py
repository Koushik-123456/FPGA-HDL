#!/usr/bin/env python3
"""
Simple VCD waveform viewer - displays signal changes from VCD files.
"""
import sys
from pathlib import Path

def parse_vcd(filename):
    """Parse VCD file and return signals and events."""
    signals = {}
    symbol_map = {}
    events = []
    current_time = 0
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    i = 0
    in_definitions = False
    
    while i < len(lines):
        line = lines[i].strip()
        
        if line == '$scope module tb $end':
            in_definitions = True
        elif line == '$upscope $end':
            in_definitions = False
        elif in_definitions and line.startswith('$var'):
            parts = line.split()
            if len(parts) >= 5:
                # $var wire WIDTH SYMBOL NAME $end
                width = int(parts[2])
                symbol = parts[3]
                name = parts[4]
                signals[name] = {'width': width, 'symbol': symbol}
                symbol_map[symbol] = name
        elif line.startswith('#'):
            current_time = int(line[1:])
        elif current_time is not None and any(c in line for c in ['0', '1', 'b', 'x', 'z']):
            # Value change
            if line and line[0] in ['0', '1', 'x', 'z']:
                sym = line[1:] if len(line) > 1 else ''
                val = line[0]
                if sym in symbol_map:
                    events.append((current_time, symbol_map[sym], val))
            elif line.startswith('b'):
                parts = line.split()
                if len(parts) >= 2:
                    val = parts[0][1:]
                    sym = parts[1]
                    if sym in symbol_map:
                        events.append((current_time, symbol_map[sym], val))
        
        i += 1
    
    return signals, events

def display_vcd(filename, num_rows=30):
    """Display VCD waveform in terminal."""
    try:
        signals, events = parse_vcd(filename)
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")
        return
    
    if not signals:
        print(f"❌ No signals found in {filename}")
        return
    
    print("\n" + "=" * 80)
    print(f"VCD Waveform Viewer: {filename}")
    print("=" * 80)
    print(f"\nSignals ({len(signals)}):")
    print("-" * 80)
    for name, info in signals.items():
        print(f"  {name:<20} width={info['width']:>2} symbol={info['symbol']}")
    
    print(f"\nValue Changes ({len(events)} total):")
    print("-" * 80)
    print(f"{'Time':<12} {'Signal':<20} {'Value':<10}")
    print("-" * 80)
    
    # Group events by time for better readability
    time_events = {}
    for time, signal, value in events:
        if time not in time_events:
            time_events[time] = []
        time_events[time].append((signal, value))
    
    count = 0
    for time in sorted(time_events.keys())[:num_rows]:
        for signal, value in time_events[time]:
            # Format binary values nicely
            if value.startswith('b'):
                display_val = f"0b{value[1:]}"
            else:
                display_val = value
            print(f"{time:<12} {signal:<20} {display_val:<10}")
            count += 1
    
    if len(time_events) > num_rows:
        print(f"\n... ({len(events) - num_rows} more changes)")
    
    print("\n" + "=" * 80)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: vcd_viewer.py <vcd_file>")
        print("\nExamples:")
        print("  python vcd_viewer.py wave/alu_4bit.vcd")
        print("  python vcd_viewer.py wave/mux4to1.vcd")
        print("  python vcd_viewer.py wave/counter3.vcd")
        sys.exit(1)
    
    vcd_file = sys.argv[1]
    num_rows = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    
    if not Path(vcd_file).exists():
        print(f"❌ File not found: {vcd_file}")
        sys.exit(1)
    
    display_vcd(vcd_file, num_rows)
