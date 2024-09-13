## SPICE Simulation

1. Ensure there is **hspice** in the current environment.
2. Put the sub-circuit definition to `./Spice/Cirs/models/XXX.cir`.
3. Change the parameters (input transition time, load capacitance) in `./Spice/Cirs/generated/generate_hspice.py`.
4. Choose the output data (for train or test) in `./Spice/Cirs/results/post_process4.py`
5. run `python ./Spice/Cirs/main.py`.

*PS: You can run `python ./Spice/Tools/delete_files.py` to delete complex process files.*

## Neural ODE

This repo refers to https://github.com/EmilienDupont/augmented-neural-odes.

* The Dataset for Neural ODE model is saved in `./Spice/Libs/Ours/Dataset`.
* run `python ./NODE/main.py`.
