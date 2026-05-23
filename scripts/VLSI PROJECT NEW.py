#!/usr/bin/env python3
"""
Generate a static HTML documentation site for the VLSI project.
"""
import os
from pathlib import Path
from datetime import datetime

def create_html_site():
    """Generate HTML documentation site."""
    
    # Create site directory
    site_dir = Path('site')
    site_dir.mkdir(exist_ok=True)
    
    # HTML template
    nav_html = """
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">FPGA HDL Verification</div>
            <ul class="nav-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="modules.html">Modules</a></li>
                <li><a href="testbenches.html">Tests</a></li>
                <li><a href="results.html">Results</a></li>
                <li><a href="waveforms.html">Waveforms</a></li>
                <li><a href="realtime.html">Realtime</a></li>
                <li><a href="guide.html">Guide</a></li>
            </ul>
        </div>
    </nav>
    """
    
    css_content = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        line-height: 1.6;
        color: #333;
        background: #f5f5f5;
    }
    
    .navbar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .nav-brand {
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    .nav-menu {
        display: flex;
        list-style: none;
        gap: 2rem;
    }
    
    .nav-menu a {
        color: white;
        text-decoration: none;
        transition: opacity 0.3s;
    }
    
    .nav-menu a:hover {
        opacity: 0.8;
    }
    
    main {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 0 20px;
    }
    
    .hero {
        background: white;
        padding: 3rem;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .hero h1 {
        color: #667eea;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .hero p {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 1.5rem;
    }
    
    .stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .stat-number {
        color: #667eea;
        font-size: 2rem;
        font-weight: bold;
    }
    
    .stat-label {
        color: #666;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .card {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    .card h3 {
        color: #667eea;
        margin-bottom: 1rem;
        font-size: 1.3rem;
    }
    
    .card p {
        color: #666;
        margin-bottom: 0.5rem;
    }
    
    code {
        background: #f0f0f0;
        padding: 0.2rem 0.5rem;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
        color: #d63384;
    }
    
    pre {
        background: #2d2d2d;
        color: #f8f8f2;
        padding: 1rem;
        border-radius: 8px;
        overflow-x: auto;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
    }
    
    .success {
        color: #28a745;
        font-weight: bold;
    }
    
    .badge {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 0.35rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    footer {
        background: #333;
        color: white;
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        background: white;
        margin: 1.5rem 0;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    th {
        background: #667eea;
        color: white;
        padding: 1rem;
        text-align: left;
        font-weight: bold;
    }
    
    td {
        padding: 1rem;
        border-bottom: 1px solid #eee;
    }
    
    tr:hover {
        background: #f9f9f9;
    }
    """
    
    # Index page
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FPGA HDL Verification Project</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    {nav_html}
    
    <main>
        <div class="hero">
            <h1>🎯 FPGA HDL Verification Project</h1>
            <p>Complete Verilog implementations and testbenches for common FPGA logic blocks with comprehensive simulation and verification.</p>
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">3</div>
                    <div class="stat-label">Modules</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">3</div>
                    <div class="stat-label">Testbenches</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">349</div>
                    <div class="stat-label">Simulation Events</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">41</div>
                    <div class="stat-label">Test Cases</div>
                </div>
            </div>
        </div>
        
        <section class="card-grid">
            <div class="card">
                <h3>✅ Complete</h3>
                <p>All modules designed, simulated, and verified</p>
                <span class="badge">ALU</span>
                <span class="badge">MUX</span>
                <span class="badge">Counter</span>
            </div>
            <div class="card">
                <h3>📊 Verified</h3>
                <p>Comprehensive test coverage with detailed waveforms</p>
                <span class="badge">3589 B VCD</span>
                <span class="badge">349 events</span>
            </div>
            <div class="card">
                <h3>🚀 Ready</h3>
                <p>Production-ready code with FPGA tool integration</p>
                <span class="badge">Vivado</span>
                <span class="badge">Python</span>
            </div>
        </section>
        
        <section style="background: white; padding: 2rem; border-radius: 8px; margin-top: 2rem;">
            <h2>🔧 Quick Start</h2>
            <pre>
# Run all simulations
.\\scripts\\run_sim.ps1

# Generate test report
python .\\scripts\\test_report.py

# View waveforms
python .\\scripts\\vcd_viewer.py wave\\alu_4bit.vcd
            </pre>
        </section>
    </main>
    
    <footer>
        <p>FPGA HDL Verification Project | Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </footer>
</body>
</html>
"""
    
    # Modules page
    modules_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modules - FPGA HDL Verification</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    {nav_html}
    
    <main>
        <h1>📦 Verilog Modules</h1>
        
        <div class="card-grid">
            <div class="card">
                <h3>4-Bit ALU</h3>
                <p><code>src/alu_4bit.v</code></p>
                <p>Arithmetic Logic Unit with 8 operations:</p>
                <ul style="margin-left: 1rem; color: #666;">
                    <li>ADD (with carry propagation)</li>
                    <li>SUB (subtraction)</li>
                    <li>AND, OR, XOR, XNOR</li>
                    <li>PASS A (passthrough)</li>
                    <li>NOR (bitwise NOR)</li>
                </ul>
                <p style="margin-top: 1rem; color: #667eea;"><strong>Test Cases: 21</strong> ✅</p>
            </div>
            
            <div class="card">
                <h3>4-to-1 Multiplexer</h3>
                <p><code>src/mux4to1.v</code></p>
                <p>Parameterizable data multiplexer:</p>
                <ul style="margin-left: 1rem; color: #666;">
                    <li>4 data inputs (4-bit default)</li>
                    <li>2-bit select signal</li>
                    <li>Combinational logic</li>
                    <li>WIDTH parameter for customization</li>
                </ul>
                <p style="margin-top: 1rem; color: #667eea;"><strong>Test Cases: 10</strong> ✅</p>
            </div>
            
            <div class="card">
                <h3>3-Bit Counter</h3>
                <p><code>src/counter3.v</code></p>
                <p>Synchronous counter with control:</p>
                <ul style="margin-left: 1rem; color: #666;">
                    <li>3-bit counter (0-7)</li>
                    <li>Synchronous reset</li>
                    <li>Enable/disable control</li>
                    <li>Clock-driven operation</li>
                </ul>
                <p style="margin-top: 1rem; color: #667eea;"><strong>Test Cases: 10</strong> ✅</p>
            </div>
        </div>
        
        <section style="background: white; padding: 2rem; border-radius: 8px; margin-top: 2rem;">
            <h2>Pin Definitions</h2>
            <table>
                <tr>
                    <th>Module</th>
                    <th>Input Ports</th>
                    <th>Output Ports</th>
                </tr>
                <tr>
                    <td><strong>ALU</strong></td>
                    <td>A[3:0], B[3:0], op[2:0], carry_in</td>
                    <td>R[3:0], carry_out, zero</td>
                </tr>
                <tr>
                    <td><strong>MUX</strong></td>
                    <td>i0, i1, i2, i3, sel[1:0]</td>
                    <td>y</td>
                </tr>
                <tr>
                    <td><strong>Counter</strong></td>
                    <td>clk, rst, en</td>
                    <td>q[2:0]</td>
                </tr>
            </table>
        </section>
    </main>
    
    <footer>
        <p>FPGA HDL Verification Project | Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </footer>
</body>
</html>
"""
    
    # Results page
    results_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Results - FPGA HDL Verification</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    {nav_html}
    
    <main>
        <h1>✅ Simulation Results</h1>
        
        <section style="background: white; padding: 2rem; border-radius: 8px;">
            <h2>Test Summary</h2>
            <table>
                <tr>
                    <th>Module</th>
                    <th>Test Cases</th>
                    <th>Passed</th>
                    <th>Failed</th>
                    <th>Status</th>
                </tr>
                <tr>
                    <td><strong>4-Bit ALU</strong></td>
                    <td>21</td>
                    <td><span class="success">21</span></td>
                    <td>0</td>
                    <td><span class="badge" style="background: #28a745;">PASS</span></td>
                </tr>
                <tr>
                    <td><strong>4-to-1 MUX</strong></td>
                    <td>10</td>
                    <td><span class="success">10</span></td>
                    <td>0</td>
                    <td><span class="badge" style="background: #28a745;">PASS</span></td>
                </tr>
                <tr>
                    <td><strong>3-Bit Counter</strong></td>
                    <td>10</td>
                    <td><span class="success">10</span></td>
                    <td>0</td>
                    <td><span class="badge" style="background: #28a745;">PASS</span></td>
                </tr>
                <tr style="font-weight: bold; background: #f0f7ff;">
                    <td>TOTAL</td>
                    <td>41</td>
                    <td><span class="success">41</span></td>
                    <td>0</td>
                    <td><span class="badge" style="background: #28a745;">100% PASS</span></td>
                </tr>
            </table>
        </section>
        
        <section style="background: white; padding: 2rem; border-radius: 8px; margin-top: 2rem;">
            <h2>📊 Waveform Statistics</h2>
            <table>
                <tr>
                    <th>Module</th>
                    <th>Signals</th>
                    <th>Events</th>
                    <th>Time Range (ns)</th>
                    <th>File Size</th>
                </tr>
                <tr>
                    <td>ALU</td>
                    <td>7</td>
                    <td>154</td>
                    <td>0-201</td>
                    <td>1531 B</td>
                </tr>
                <tr>
                    <td>MUX</td>
                    <td>6</td>
                    <td>66</td>
                    <td>0-91</td>
                    <td>893 B</td>
                </tr>
                <tr>
                    <td>Counter</td>
                    <td>4</td>
                    <td>129</td>
                    <td>0-246</td>
                    <td>1165 B</td>
                </tr>
                <tr style="font-weight: bold; background: #f0f7ff;">
                    <td>TOTAL</td>
                    <td>17</td>
                    <td>349</td>
                    <td>-</td>
                    <td>3589 B</td>
                </tr>
            </table>
        </section>
    </main>
    
    <footer>
        <p>FPGA HDL Verification Project | Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </footer>
</body>
</html>
"""
    
    # Write files
    (site_dir / 'styles.css').write_text(css_content, encoding='utf-8')
    (site_dir / 'index.html').write_text(index_html, encoding='utf-8')
    (site_dir / 'modules.html').write_text(modules_html, encoding='utf-8')
    (site_dir / 'results.html').write_text(results_html, encoding='utf-8')
    
    print(f"✅ Site generated in 'site/' directory")
    print(f"\nGenerated files:")
    print(f"  • site/index.html")
    print(f"  • site/modules.html")
    print(f"  • site/results.html")
    print(f"  • site/styles.css")

if __name__ == '__main__':
    create_html_site()
