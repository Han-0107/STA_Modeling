import os
import re
import itertools
import numpy as np
import subprocess

def new_cir(new_vol, new_cap, cir_path, transition_time):
    with open(cir_path, 'r') as file:
        hspice_code = file.read()

    new_val = new_vol/2
    new_val = round(new_val, 3)
    new_vol = round(new_vol, 3)
    # VOL
    hspice_code = re.sub(r'(\.param VOL=)(\d+(\.\d+)?)', r'\g<1>{}'.format(new_vol), hspice_code)
    # transition time
    hspice_code = re.sub(r'driver_5p', f'driver_{transition_time}p', hspice_code)
    # exit(0)
    # Cout
    hspice_code = re.sub(r'(Cout y 0 )(\d+(\.\d+)?p)', r'\g<1>{:.5f}p'.format(new_cap * 1e12), hspice_code)

    # VAL
    hspice_code = re.sub(r'(VAL=)(\d+(\.\d+)?)', r'\g<1>{}'.format(new_val), hspice_code)

    # output txt
    new_index = f'nand_VOL_{new_vol}_Trans_{transition_time}ps_Cap_{new_cap * 1e15:.2f}ff.txt'
    hspice_code = re.sub(r'(\./Delays/nand_VOL_)(\d+(\.\d+)?V)', r'\g<1>{}'.format(new_index), hspice_code)

    # save
    new_dir = os.path.join(os.path.dirname('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/'), 'generated')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    new_filename = new_index.split('.txt')[0]
    with open(new_dir + '/' + f'{new_filename}.cir', 'w') as file:
        file.write(hspice_code)

def generate(cir_path):
    transition_time = [10, 20, 55]
    subprocess.run(["python",
                    "/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/models/waveform/gen_waveform.py",
                    str(transition_time)])

    vols = np.arange(0.7, 0.9, 0.1)
    caps = np.arange(2.8e-15, 3e-15, 0.1e-15)
    for i in transition_time:
        for v, cap in itertools.product(vols, caps):
            new_cir(v, cap, cir_path, i)
    
    print('\033[1;32mHSPICE Generator\033[0m: All .cir files have been generated')

cir_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/models/nand_model.cir'
generate(cir_path)
