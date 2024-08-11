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
                         r'\g<1>{:.5f}n {:.5f}n'.format(new_pulse_rise_fall * 1e9, new_pulse_rise_fall * 1e9),
                         hspice_code)

    # Cout
    hspice_code = re.sub(r'(Cout y 0 )(\d+(\.\d+)?p)', r'\g<1>{:.5f}p'.format(new_cap * 1e12), hspice_code)

    # VAL
    hspice_code = re.sub(r'(VAL=)(\d+(\.\d+)?)', r'\g<1>{}'.format(new_val), hspice_code)

    # output txt
    new_index = f'nand_VOL_{new_vol}_Trans_{new_pulse_rise_fall * 1e12:.2f}p_Cap_{new_cap * 1e15:.2f}ff.txt'
    hspice_code = re.sub(r'(\./Delays/nand_VOL_)(\d+(\.\d+)?V)', r'\g<1>{}'.format(new_index), hspice_code)

    # save
    new_dir = os.path.join(os.path.dirname(cir_path), 'generated')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    new_filename = new_index.split('.txt')[0]
    with open(new_dir + '/' + f'{new_filename}.cir', 'w') as file:
        file.write(hspice_code)

def main(cir_path):

    vols = [0.63, 0.7, 0.77]
    pulses = [2.5e-12, 7.5e-12, 10e-12]
    caps = [0.72e-15, 1.44e-15, 2.88e-15]

    for v, pulse, cap in itertools.product(vols, pulses, caps):
        new_cir(v, pulse, cap, cir_path)
    
    print('All .cir files are generated...')


if __name__ == '__main__':
    cir_path = '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/nand_model.cir'
    main(cir_path)


