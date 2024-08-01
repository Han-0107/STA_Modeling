import os.path
import re
import itertools

def new_cir(new_vol, new_pulse_rise_fall, new_cap,  cir_path):
    with open(cir_path, 'r') as file:
        hspice_code = file.read()

    new_val = new_vol/2
    # VOL
    hspice_code = re.sub(r'(\.param VOL=)(\d+(\.\d+)?)', r'\g<1>{}'.format(new_vol), hspice_code)

    # transition time
    hspice_code = re.sub(r'(PULSE\(0 VOL 0 )(\d+(\.\d+)?n) (\d+(\.\d+)?n)',
                         r'\g<1>{:.1f}n {:.1f}n'.format(new_pulse_rise_fall * 1e9, new_pulse_rise_fall * 1e9),
                         hspice_code)

    # Cout
    hspice_code = re.sub(r'(Cout y 0 )(\d+(\.\d+)?p)', r'\g<1>{:.1f}p'.format(new_cap * 1e12), hspice_code)

    # VAL
    hspice_code = re.sub(r'(VAL=)(\d+(\.\d+)?)', r'\g<1>{}'.format(new_val), hspice_code)

    # output txt
    new_index = f'nand_VOL_{new_vol}_Trans_{new_pulse_rise_fall * 1e9:.1f}n_Cap_{new_cap * 1e12:.1f}p.txt'
    hspice_code = re.sub(r'(\./Delays/nand_VOL_)(\d+(\.\d+)?V)', r'\g<1>{}'.format(new_index), hspice_code)

    # save
    new_dir = os.path.join(os.path.dirname(cir_path), 'gen_cir')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    new_filename = new_index.split('.txt')[0]
    with open(new_dir + '\\' + f'{new_filename}.cir', 'w') as file:
        file.write(hspice_code)

def main(cir_path):

    vols = [1,2,3,4,5]
    pulses = [2e-9,3e-9,4e-9,5e-9]
    caps = [0.2e-12,0.3e-12,0.4e-12,0.5e-12]


    for v, pulse, cap in itertools.product(vols, pulses, caps):
        new_cir(v, pulse, cap, cir_path)


if __name__ == '__main__':
    cir_path = 'D:\data\expriment\STA modeling\\nand\\nand\Circuits\\nand_1.2V.cir'
    main(cir_path)


