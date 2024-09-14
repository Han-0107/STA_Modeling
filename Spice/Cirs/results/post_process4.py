import os
import pandas as pd

file_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot/All_data.csv'
data_folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Ours/Dataset/train'
os.makedirs(data_folder_path, exist_ok=True)
df = pd.read_csv(file_path)
vol_values = df['VOL'].unique()
gate_values = df['Gate'].unique()

def get_real_code(logic_gate):
    logic_gate = int(logic_gate)
    if logic_gate == 1:
        return 'AND'
    elif logic_gate == 10:
        return 'NAND'
    elif logic_gate == 11:
        return 'NOR'
    elif logic_gate == 100:
        return 'NOT'
    elif logic_gate == 101:
        return 'OR'
    elif logic_gate == 110:
        return 'XNOR'
    elif logic_gate == 111:
        return 'XOR'

def replace_failed_with_zero(x):
    try:
        return float(x)
    except ValueError:
        return 0

def to_three_dimensional(value):
    binary_str = str(value)
    padded_binary_str = binary_str.zfill(3)
    bit_list = [int(bit) for bit in padded_binary_str]
    return bit_list


for gate_value in gate_values:
    for vol_value in vol_values:
        subset_df = df[(df['VOL'] == vol_value) & (df['Gate'] == gate_value)].copy()
        new_df = subset_df[['Gate', 'VOL', 'Trans', 'Cap', 'Tphl', 'Tplh']].copy()
        df_gate = subset_df['Gate'].apply(to_three_dimensional).apply(pd.Series)
        df_gate.columns = ['Gate_0', 'Gate_1', 'Gate_2']
        final_df = pd.concat([df_gate, subset_df.drop('Gate', axis=1)], axis=1)
        formatted_data = final_df.values.tolist()
        gate_name = get_real_code(gate_value)
        new_file = f'{gate_name}_Vol_{vol_value}.txt'
        new_file_path = os.path.join(data_folder_path, new_file)

        with open(new_file_path, 'w') as file:
            file.write('[\n')

            for i in range(len(formatted_data)):
                row_data = ', '.join(f"{formatted_data[i][j]}" for j in range(8))
                if i == len(formatted_data) - 1:
                    file.write('    [{}]\n'.format(row_data))
                else:
                    file.write('    [{}], \n'.format(row_data))

            file.write(']\n')

print('\033[1;32mPost Process 4\033[0m: Data for Neural ODE have been generated and saved to', data_folder_path)
