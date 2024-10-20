## Design Compiler如何自定义库文件进行综合和时序分析？

* 读入目标库：set target_library "./libs/cells_1.0v.db ./libs/cells_1.2v.db"
* 读入链接库：set link_library "* ./libs/cells_1.0v.db ./libs/cells_1.2v.db"
* 读入verilog设计：read_verilog ./cirs/nand.v
* 建立关联：link
* 编译：compile
* 读入sdc文件：read_sdc ./cirs/nand.sdc
* 创建运作条件：create_operating_conditions -name My_1.1V_Condition -voltage 1.1 -process 1.0 -temperature 27 -library [list cells_1.0v cells_1.2v]
* 使用运作条件：set_operating_conditions My_1.1V_Condition
* 设置负载：set_load 1.0 [get_ports y]
* 查看使用的cell：report_cell
* 查看时序报告：report_timing

transition time在.sdc文件中进行定义，load capacitance通过set_load进行定义

## Library Compiler将.lib文件转换为.db文件

* lc_shell> read_lib xxx.lib
* lc_shell > write_lib -format db xxx -output xx.db
