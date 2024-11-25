# Design Compiler flow

## How does Design Compiler customize library files for synthesis and timing analysis?

* Read the target library: `set target_library "./libs/asap7/asap7sc7p5t_INVBUF_RVT_FF_ccs_211120.db ./libs/asap7/asap7sc7p5t_INVBUF_RVT_SS_ccs_211120.db ./libs/asap7/asap7sc7p5t_SIMPLE_RVT_FF_ccs_211120.db ./libs/asap7/asap7sc7p5t_SIMPLE_RVT_SS_ccs_211120.db"`
* Read link library: `set link_library "* ./libs/asap7/asap7sc7p5t_INVBUF_RVT_FF_ccs_211120.db ./libs/asap7/asap7sc7p5t_INVBUF_RVT_SS_ccs_211120.db ./libs/asap7/asap7sc7p5t_SIMPLE_RVT_FF_ccs_211120.db ./libs/asap7/asap7sc7p5t_SIMPLE_RVT_SS_ccs_211120.db"`
* Read in a Verilog design: `read_verilog ./cirs/nand.v`
* Create a link: `link`
* Compile: `compile`
* Read in the sdc file: `read_sdc ./cirs/nand.sdc`
* Create operating conditions: `create_operating_conditions -name New_Condition -voltage 0.7 -process 1.0 -temperature 25 -library [list asap7sc7p5t_INVBUF_RVT_FF_ccs_211120 asap7sc7p5t_INVBUF_RVT_SS_ccs_211120 asap7sc7p5t_SIMPLE_RVT_FF_ccs_211120 asap7sc7p5t_SIMPLE_RVT_SS_ccs_211120]`
* To use custom operating conditions: `set_operating_conditions New_Condition`
* Setting the load capacitance: `set_load 1.0 [get_ports y]`
* View the cells used: `report_cell`
* View the timing report: `report_timing`

The transition time is defined in the `.sdc` file, and the load capacitance is defined by `set_load`.

## How does Library Compiler converts .lib files to .db files?

* `lc_shell> read_lib xxx.lib`
* `lc_shell > write_lib -format db xxx -output xx.db`

![DC flow](DC_flow/DC.PNG)
