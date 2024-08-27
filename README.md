## SPICE Simulation

1. Ensure there is **hspice** in the current environment.
2. Put the sub-circuit definition to `./Circuits/XXX.cir`.
3. Change the parameters (input transition time, load capacitance) in `gates/Circuits/generated/generate_hspice.py`.
4. run `python ./gates/Circuits/main.py`.

## Neural ODE

This repo refers to https://github.com/EmilienDupont/augmented-neural-odes

* run `python main.py`
