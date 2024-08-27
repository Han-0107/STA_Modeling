import os
import pandas as pd

file_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot/All_data.csv'
df = pd.read_csv(file_path)
vol_values = df['VOL'].unique()


def replace_failed_with_zero(x):
    try:
        return float(x)
    except ValueError:
        return -1


df['Tplh'] = df['Tplh'].map(replace_failed_with_zero)
df['Tphl'] = df['Tphl'].map(replace_failed_with_zero)

# 定义文件夹路径以分别存储CSV文件和pivot CSV文件
normal_folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results'
pivot_folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot'

# 创建文件夹，如果不存在
os.makedirs(normal_folder_path, exist_ok=True)
os.makedirs(pivot_folder_path, exist_ok=True)

# 创建并保存子集为单独的 CSV 文件
for vol_value in vol_values:
    subset_df = df[df['VOL'] == vol_value].copy()
    tplh_df = subset_df[['Trans', 'Cap', 'Tplh']].copy()
    tplh_df['Tplh'] = tplh_df['Tplh'].apply(lambda x: round(float(x) * (10 ** 9), 5))
    tplh_file = f'Tplh_vol_{vol_value}_pivot.csv'
    tplh_df.to_csv(os.path.join(pivot_folder_path, tplh_file), index=False)
    tphl_df = subset_df[['Trans', 'Cap', 'Tphl']].copy()
    tphl_df['Tphl'] = tphl_df['Tphl'].apply(lambda x: round(float(x) * (10 ** 9), 5))
    tphl_file = f'Tphl_vol_{vol_value}_pivot.csv'
    tphl_df.to_csv(os.path.join(pivot_folder_path, tphl_file), index=False)

for filename in os.listdir(pivot_folder_path):
    if filename.startswith('Tplh_vol_') and filename.endswith('_pivot.csv'):
        file_path = os.path.join(pivot_folder_path, filename)
        df = pd.read_csv(file_path)
        pivot_df = df.pivot(index='Trans', columns='Cap', values='Tplh')
        pivot_file = filename.replace('_pivot.csv', '.csv')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df = pd.read_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df.columns = pivot_df.columns.str.replace('Trans', '')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file), index=False)

    if filename.startswith('Tphl_vol_') and filename.endswith('_pivot.csv'):
        file_path = os.path.join(pivot_folder_path, filename)
        df = pd.read_csv(file_path)
        pivot_df = df.pivot(index='Trans', columns='Cap', values='Tphl')
        pivot_file = filename.replace('_pivot.csv', '.csv')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df = pd.read_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df.columns = pivot_df.columns.str.replace('Trans', '')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file), index=False)

print('\033[1;32mPost Process\033[0m: CSV files have been generated')
