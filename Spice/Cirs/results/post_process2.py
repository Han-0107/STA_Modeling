import os
import pandas as pd

file_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot/All_data.csv'
df = pd.read_csv(file_path)
vol_values = df['VOL'].unique()
gate_values = df['Gate'].unique()

def replace_failed_with_zero(x):
    try:
        return float(x)
    except ValueError:
        return 0

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

df['Tplh'] = df['Tplh'].map(replace_failed_with_zero)
df['Tphl'] = df['Tphl'].map(replace_failed_with_zero)

# 定义文件夹路径以分别存储CSV文件和pivot CSV文件
normal_folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/csv'
pivot_folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot'

# 创建文件夹，如果不存在
os.makedirs(normal_folder_path, exist_ok=True)
os.makedirs(pivot_folder_path, exist_ok=True)

# 创建并保存子集为单独的 CSV 文件

for gate_value in gate_values:
    for vol_value in vol_values:
        subset_df = df[(df['VOL'] == vol_value) & (df['Gate'] == gate_value)].copy()
        tplh_df = subset_df[['Trans', 'Cap', 'Tplh']].copy()
        gate_name = get_real_code(gate_value)
        tplh_file = f'{gate_name}_Tplh_Vol_{vol_value}_Pivot.csv'
        tplh_df.to_csv(os.path.join(pivot_folder_path, tplh_file), index=False)
        tphl_df = subset_df[['Trans', 'Cap', 'Tphl']].copy()
        gate_name = get_real_code(gate_value)
        tphl_file = f'{gate_name}_Tphl_Vol_{vol_value}_Pivot.csv'
        tphl_df.to_csv(os.path.join(pivot_folder_path, tphl_file), index=False)

for filename in os.listdir(pivot_folder_path):
    if 'Tplh' in filename and filename.endswith('_Pivot.csv'):
        file_path = os.path.join(pivot_folder_path, filename)
        df = pd.read_csv(file_path)
        pivot_df = df.pivot(index='Trans', columns='Cap', values='Tplh')
        pivot_file = filename.replace('_Pivot.csv', '.csv')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df = pd.read_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df.columns = pivot_df.columns.str.replace('Trans', '')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file), index=False)

    if 'Tphl' in filename and filename.endswith('_Pivot.csv'):
        file_path = os.path.join(pivot_folder_path, filename)
        df = pd.read_csv(file_path)
        pivot_df = df.pivot(index='Trans', columns='Cap', values='Tphl')
        pivot_file = filename.replace('_Pivot.csv', '.csv')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df = pd.read_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df.columns = pivot_df.columns.str.replace('Trans', '')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file), index=False)

print('\033[1;32mPost Process 2\033[0m: CSV files have been generated')
