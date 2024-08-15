import os
import pandas as pd
from openpyxl import load_workbook

file_path = '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results/pivot/All_data.csv'
df = pd.read_csv(file_path)
vol_values = df['VOL'].unique()

def replace_failed_with_zero(x):
    try:
        return float(x)
    except ValueError:
        return 0
df = df.map(replace_failed_with_zero)
# 定义文件夹路径以分别存储CSV文件和pivot CSV文件
normal_folder_path = '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results'
pivot_folder_path = '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results/pivot'

# 创建文件夹，如果不存在
os.makedirs(normal_folder_path, exist_ok=True)
os.makedirs(pivot_folder_path, exist_ok=True)

# 创建并保存子集为单独的 CSV 文件
for vol_value in vol_values:
    subset_df = df[df['VOL'] == vol_value].copy()
    output_file = f'vol_{vol_value}_pivot.csv'
    # 使用 .loc 来安全地修改数据
    subset_df.loc[:, 'Tplh'] = subset_df['Tplh'].apply(lambda x: round(float(x) * (10 ** 9), 5))
    subset_df.to_csv(os.path.join(pivot_folder_path, output_file), index=False, columns=['Trans', 'Cap', 'Tplh'])

for filename in os.listdir(pivot_folder_path):
    if filename.startswith('vol_') and filename.endswith('_pivot.csv'):
        file_path = os.path.join(pivot_folder_path, filename)
        df = pd.read_csv(file_path)
        pivot_df = df.pivot(index='Trans', columns='Cap', values='Tplh')
        pivot_file = filename.replace('_pivot.csv', '.csv')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file))
        # 加载 CSV 文件并清空 A1 单元格
        pivot_df = pd.read_csv(os.path.join(normal_folder_path, pivot_file))
        pivot_df.columns = pivot_df.columns.str.replace('Trans','')
        pivot_df.to_csv(os.path.join(normal_folder_path, pivot_file), index=False)

print('CSV files have been generated')
