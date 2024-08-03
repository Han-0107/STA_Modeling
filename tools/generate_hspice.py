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
                         r'\g<1>{:.1f}n {:.1f}n'.format(new_pulse_rise_fall * 1e12, new_pulse_rise_fall * 1e12),
                         hspice_code)

    # Cout
    hspice_code = re.sub(r'(Cout y 0 )(\d+(\.\d+)?p)', r'\g<1>{:.1f}p'.format(new_cap * 1e15), hspice_code)

    # VAL
    hspice_code = re.sub(r'(VAL=)(\d+(\.\d+)?)', r'\g<1>{}'.format(new_val), hspice_code)

    # output txt
    new_index = f'nand_VOL_{new_vol}_Trans_{new_pulse_rise_fall * 1e12:.1f}n_Cap_{new_cap * 1e15:.2f}p.txt'
    hspice_code = re.sub(r'(\./Delays/nand_VOL_)(\d+(\.\d+)?V)', r'\g<1>{}'.format(new_index), hspice_code)

    # save
    new_dir = os.path.join(os.path.dirname(cir_path), 'generated')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    new_filename = new_index.split('.txt')[0]
    with open(new_dir + '/' + f'{new_filename}.cir', 'w') as file:
        file.write(hspice_code)

def main(cir_path):

    vols = [0.6, 0.63, 0.7, 0.73, 0.77, 0.8]
    pulses = [0, 2.5e-12, 5e-12, 7.5e-12, 10e-12, 15e-12, 20e-12, 40e-12, 80e-12, 160e-12, 320e-12, 340e-12]
    caps = [0.36e-15, 0.72e-15, 1.44e-15, 2.88e-15, 4.32e-15, 5.76e-15, 11.52e-15, 23.04e-15, 34.56e-15, 46.08e-15, 92.16e-15, 115.2e-15]

    for v, pulse, cap in itertools.product(vols, pulses, caps):
        new_cir(v, pulse, cap, cir_path)


if __name__ == '__main__':
    cir_path = '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/nand_model.cir'
    main(cir_path)


