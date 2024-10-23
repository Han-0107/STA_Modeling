# Design Compiler flow

## How does Design Compiler customize library files for synthesis and timing analysis?

* Read the target library: `set target_library "./libs/cells_1.0v.db ./libs/cells_1.2v.db"`
* Read link library: `set link_library "* ./libs/cells_1.0v.db ./libs/cells_1.2v.db"`
* Read in a Verilog design: `read_verilog ./cirs/nand.v`
* Create a link: `link`
* Compile: `compile`
* Read in the sdc file: `read_sdc ./cirs/nand.sdc`
* Create operating conditions: `create_operating_conditions -name My_1.1V_Condition -voltage 1.1 -process 1.0 -temperature 27 -library [list cells_1.0v cells_1.2v]`
* To use custom operating conditions: `set_operating_conditions My_1.1V_Condition`
* Setting the load capacitance: `set_load 1.0 [get_ports y]`
* View the cells used: `report_cell`
* View the timing report: `report_timing`

The transition time is defined in the `.sdc` file, and the load capacitance is defined by `set_load`.

## How does Library Compiler converts .lib files to .db files?

* `lc_shell> read_lib xxx.lib`
* `lc_shell > write_lib -format db xxx -output xx.db`

![DC flow](DC_flow/DC.PNG)
