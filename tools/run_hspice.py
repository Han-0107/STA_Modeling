import os
import subprocess
from tqdm import tqdm

CIR_DIR = "/data/yaohuihan/Research/STA_Modeling/gates/Circuits/generated"

def run_hspice_on_files(directory):
    cir_files = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith(".cir")]

    for cir_file in tqdm(cir_files, desc="Running HSPICE simulations"):
        with open(os.devnull, 'w') as devnull:
            subprocess.run(["hspice", cir_file], stdout=devnull, stderr=devnull)
    print("All HSPICE simulations are complete.")

if __name__ == "__main__":
    run_hspice_on_files(CIR_DIR)
