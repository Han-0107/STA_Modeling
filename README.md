## Auto SPICE Simulation

This process is designed to automatically run hspice scripts in large batches and generate various datasets for training. It can automatically generate waveforms and interpolate automatically to improve the accuracy of input signals.

1. Ensure there is **hspice** in the current environment.
2. Put the sub-circuit definition to `./Spice/Cirs/models/XXX.cir`.
3. Change the parameters (input transition time, load capacitance) in `./Spice/Cirs/generated/generate_hspice.py`.
4. run `python ./Spice/Cirs/main.py`.

## Splitting Data

1. Change the parameters in `./Spice/Libs/Dataset/split_data.py` to decide which voltage is for train or test
2. Run `python ./Spice/Libs/Dataset/split_data.py` to split data.

## Data Format

Now, we represent the simulation result of a cell by a vector. The **type** of cell is represented by the one-hot code composed of the first three elements of the vector. The **voltage**, **load capacitance** and **input transition time** of the cell are in the 4th and 5th bits respectively. The **time propagation of high to low** (tphl) and **time propagation of low to high** (tplh) obtained by hspice simulation are stored in the last two bits respectively.

## Neural ODE

This repo refers to https://github.com/EmilienDupont/augmented-neural-odes. The Dataset for Neural ODE model is saved in `./Spice/Libs/Dataset`.

1. Run `python ./NODE/train.py`, the log of training will be stored in `./NODE/log`. You can examine them in [TensorBoard](https://www.tensorflow.org/tensorboard).
2. Run `python ./NODE/test.py`, you can choose a model manually.