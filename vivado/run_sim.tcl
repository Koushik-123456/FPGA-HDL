# Vivado helper: create a project and launch behavioral simulation
set proj_name fpga_verification
set proj_dir [file join [pwd] "vivado_proj"]
file mkdir $proj_dir
create_project $proj_name $proj_dir -part xc7a35tcsg324-1 ;# edit the part to match your board

add_files -norecurse [list ../src/alu_4bit.v ../src/mux4to1.v ../src/counter3.v ../tb/alu_4bit_tb.v ../tb/mux4to1_tb.v ../tb/counter3_tb.v]
set_property top tb_alu_4bit [get_files ../tb/alu_4bit_tb.v]

launch_simulation
