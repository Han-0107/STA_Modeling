
.subckt AND2X1 Y A B vdd gnd
M0 a_2_6# A vdd vdd pmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B a_2_6# vdd pmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_6# vdd vdd pmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_9_6# A a_2_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M4 gnd B a_9_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y a_2_6# gnd gnd nmos w=0.25u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
.ends AND2X1

.subckt INVX1 Y A vdd gnd
M0 Y A vdd vdd pmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y A gnd gnd nmos w=0.25u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
.ends INVX1

.subckt NAND2X1 Y A B vdd gnd
M0 Y A vdd vdd pmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B Y vdd pmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_9_6# A gnd gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M3 Y B a_9_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
.ends NAND2X1

.subckt NOR2X1 Y A B vdd gnd
M0 a_9_54# A vdd vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y B a_9_54# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y A gnd gnd nmos w=0.25u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M3 gnd B Y gnd nmos w=0.25u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
.ends NOR2X1

.subckt OR2X1 Y A B vdd gnd
M0 a_9_54# A a_2_54# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B a_9_54# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_54# vdd vdd pmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_2_54# A gnd gnd nmos w=0.25u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M4 gnd B a_2_54# gnd nmos w=0.25u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y a_2_54# gnd gnd nmos w=0.25u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
.ends OR2X1

.subckt XNOR2X1 Y A B vdd gnd
M0 vdd A a_2_6# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_18_54# a_12_41# vdd vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_6# a_18_54# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_35_54# A Y vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd B a_35_54# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_12_41# B vdd vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M6 gnd A a_2_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_18_6# a_12_41# gnd gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M8 Y A a_18_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_35_6# a_2_6# Y gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M10 gnd B a_35_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M11 a_12_41# B gnd gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
.ends XNOR2X1

.subckt XOR2X1 Y A B vdd gnd
M0 vdd A a_2_6# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_18_54# a_13_43# vdd vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y A a_18_54# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_35_54# a_2_6# Y vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd B a_35_54# vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_13_43# B vdd vdd pmos w=1u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M6 gnd A a_2_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_18_6# a_13_43# gnd gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M8 Y a_2_6# a_18_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_35_6# A Y gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M10 gnd B a_35_6# gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
M11 a_13_43# B gnd gnd nmos w=0.5u l=0.05u
+ ad=0p pd=0u as=0p ps=0u 
.ends XOR2X1

