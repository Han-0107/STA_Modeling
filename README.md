# hspice by Python

1. Put the basic circuit to "./Circuits/XXX.cir".
2. run "python ./gates/Circuits/generated/generate_hspice.py".
3. run "python ./gates/Circuits/simulated/run_hspice.py".
4. run "python ./gates/Circuits/results/post_process.py".
5. The new .csv files are what you need.

## Transition

1. File: scp connect.yluo208@10.120.25.33:/hpc/Tech/iPDK/SAED32nm/SAED32nm_EDK/tech/hspice ./gates/Libs/SAED32nm/saed32nm.lib
2. Folder: scp -r connect.yluo208@10.120.25.33:/hpc/Tech/iPDK/SAED32nm/SAED32nm_EDK/tech ./gates/Libs/SAED32nm

## SAED32nm

1. mos: /data/yaohuihan/Research/SAED32nm/SAED32nm_EDK/tech/hspice/saed32nm.lib
2. subckt: /data/yaohuihan/Research/SAED32nm/SAED32nm_EDK/lib/stdcell_rvt/lvs/saed32nm_rvt.cdl
3. NLDM libs: /data/yaohuihan/Research/SAED32nm/SAED32nm_EDK/lib/stdcell_rvt

## SAED90nm

1. mos: /data/yaohuihan/Research/SAED90nm/SAED90nm_EDK/Digital_Standard_cell_Library/spice/spice_lib/SAED90nm.lib
2. subckt: /data/yaohuihan/Research/SAED90nm/SAED90nm_EDK/Digital_Standard_cell_Library/cdl/saed90nm.cdl
3. NLDM libs: /data/yaohuihan/Research/SAED90nm/SAED90nm_EDK/Digital_Standard_cell_Library/synopsys/models