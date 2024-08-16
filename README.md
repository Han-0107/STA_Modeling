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

## 1.2V LIBs

* INVX1: cell_fall, cell_rise
* NAND2X1: cell_rise_A, cell_fall_A, cell_rise_B, cell_fall_B
* AND2X1: cell_fall_A, cell_rise_A, cell_fall_B, cell_rise_B
* OR2X1: cell_fall_A, cell_rise_A, cell_fall_B, cell_rise_B
* NOR2X1: cell_fall_A, cell_rise_A, cell_fall_B, cell_rise_B
* XOR2X1: cell_fall_A, cell_rise_A, cell_fall_B, cell_rise_B
* XNOR2X1: cell_fall_A, cell_rise_A, cell_fall_B, cell_rise_B

## 1.1V LIBs

* INVX1: cell_fall, cell_rise
* NAND2X1: cell_rise_A, cell_fall_A, cell_rise_B, cell_fall_B
* AND2X1: cell_rise_A, cell_fall_A, cell_rise_B, cell_fall_B
* OR2X1: cell_rise_A, cell_fall_A, cell_rise_B, cell_fall_B
* NOR2X1: cell_rise_A, cell_fall_A, cell_rise_B, cell_fall_B
* XOR2X1: cell_rise_A, cell_fall_A, cell_rise_B, cell_fall_B
* XNOR2X1: 
