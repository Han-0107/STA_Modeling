import os
import subprocess
from tqdm import tqdm

CIR_DIR = "/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/generated"
HSPICE_DIR = "/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/simulated"  

def run_hspice_on_files(directory):
    cir_files = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith(".cir")]

    for cir_file in tqdm(cir_files, desc="\033[1;32mSimulator\033[0m: Running HSPICE simulations"):
        with open(os.devnull, 'w') as devnull:
            subprocess.run(["hspice", cir_file], cwd=HSPICE_DIR, stdout=devnull, stderr=devnull)
    
    print('\033[1;32mSimulator\033[0m: All simulations have been completed')

if __name__ == "__main__":
    run_hspice_on_files(CIR_DIR)
