#!/bin/bash

CIR_DIR="D:\data\expriment\STA modeling\nand\nand\Circuits\gen_cir"

for cir_file in "$CIR_DIR"/*.cir; do
    echo "Running hspice on $cir_file"
    hspice "$cir_file"
done

echo "All HSPICE simulations are complete."
