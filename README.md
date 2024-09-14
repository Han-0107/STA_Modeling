## SPICE Simulation

1. Ensure there is **hspice** in the current environment.
2. Put the sub-circuit definition to `./Spice/Cirs/models/XXX.cir`.
3. Change the parameters (input transition time, load capacitance) in `./Spice/Cirs/generated/generate_hspice.py`.
4. run `python ./Spice/Cirs/main.py`.

*PS: You can run `python ./Spice/Tools/delete_files.py` to delete complex process files.*

## Splitting Data

* Change the parameters in `./Spice/Libs/Ours/Dataset/split_data.py` to decide which voltage is for train or test
* Run `python ./Spice/Libs/Ours/Dataset/split_data.py` to split data.

## Neural ODE

This repo refers to https://github.com/EmilienDupont/augmented-neural-odes.

* The Dataset for Neural ODE model is saved in `./Spice/Libs/Ours/Dataset`.
* Run `python ./NODE/train.py`.
* Run `python ./NODE/test.py`.
