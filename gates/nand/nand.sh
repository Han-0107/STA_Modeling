#!/bin/bash

mkdir -p ./Delays
mkdir -p ./Circuits

# 查找当前目录下的所有 CIR 文件
CIR_FILES=(./Circuits/*.cir)

# 循环遍历每个 CIR 文件并运行 ngspice 仿真
for CIR_FILE in "${CIR_FILES[@]}"; do
    echo "Running ngspice simulation for ${CIR_FILE}..."
    ngspice -b "${CIR_FILE}"
    
    if [ $? -eq 0 ]; then
        echo "Simulation completed successfully for ${CIR_FILE}."
    else
        echo "Simulation failed for ${CIR_FILE}."
    fi
done

echo "All simulations completed."

