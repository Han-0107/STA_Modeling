# Input and output delay constraints
set_input_delay 2 [get_ports {a b}]
set_output_delay 2 [get_ports y]

# Set max delay (for example purposes, not strictly necessary here)
set_max_delay 100 -from [get_ports {a b}] -to [get_ports y]
