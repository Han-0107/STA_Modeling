# hspice by Python

1. Put the basic circuit to "./Circuits/XXX.cir".
2. Change the parameters in "gates/Circuits/generated/generate_hspice.py".
3. run "python ./gates/Circuits/main.py".
4. The .csv files are what you need.

## Transition

1. File: scp connect.yluo208@10.120.25.33:/hpc/Tech/iPDK/SAED32nm/SAED32nm_EDK/tech/hspice ./gates/Libs/SAED32nm/saed32nm.lib
2. Folder: scp -r connect.yluo208@10.120.25.33:/hpc/Tech/iPDK/SAED32nm/SAED32nm_EDK/tech ./gates/Libs/SAED32nm

## SAED32nm

1. mos: /data/yaohuihan/Research/SAED32nm/SAED32nm_EDK/tech/hspice/saed32nm.lib
2. subckt: /data/yaohuihan/Research/SAED32nm/SAED32nm_EDK/lib/stdcell_rvt/lvs/saed32nm_rvt.cdl
3. NLDM libs: /data/yaohuihan/Research/SAED32nm/SAED32nm_EDK/lib/stdcell_rvt

## Design Compiler如何自定义库文件进行综合和时序分析？

* 首先，读入自定义库：set target_library "gscl45nm.db", set link_library "* gscl45nm.db"
* 读入verilog设计：read_verilog adder.v
* 建立关联：link
* 编译：compile
* 读入sdc文件：read_sdc adder.sdc
* 查看使用的cell：report_cell
* 查看时序报告：report_timing

## Library Compiler将.lib文件转换为.db文件

lc_shell> read_lib xx.lib
lc_shell > write_lib -format db -output xx.db xx