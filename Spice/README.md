# Auto HSPICE Simulation

## Run

This process is designed to automatically run hspice scripts in large batches and generate various datasets for training. It can automatically generate waveforms and interpolate automatically to improve the accuracy of input signals.

1. Ensure there is **hspice** in the current environment.
2. Put the sub-circuit definition to `./Spice/Cirs/models/XXX.cir`.
3. Change the parameters (input transition time, load capacitance) in `./Spice/Cirs/generated/generate_hspice.py`.
4. run `python ./Spice/Cirs/main.py`.

## Splitting Data

1. Change the parameters in `./Spice/Libs/Dataset/split_data.py` to decide which voltage is for train or test
2. Run `python ./Spice/Libs/Dataset/split_data.py` to split data.
