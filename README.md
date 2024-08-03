# hspice by Python

1. Put the basic circuit to "./Circuits/XXX.cir".
1. run "python ./tools/generate_hspice.py".
2. Copy run_hspice.py to an empty folder (like ./Circuits/simulated/).
3. run "python run_hspice.py".
4. run "find /path/to/simulated -type f ! -name "*.mt0" -delete".
5. run "python post_process.py".
6. The .csv files are what you need.

* Review the output files!
