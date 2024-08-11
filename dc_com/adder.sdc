# Define the clock
create_clock -period 10 [get_ports clk]

# Input and output delay constraints
set_input_delay -clock [get_clocks clk] 2 [get_ports {a b}]
set_output_delay -clock [get_clocks clk] 2 [get_ports sum]

# Set max delay (for example purposes, not strictly necessary here)
set_max_delay 10 -from [get_ports {a b}] -to [get_ports sum]

# Define timing exception (if any)
# Example: false path between specific registers
#set_false_path -from [get_ports a] -to [get_ports b]
