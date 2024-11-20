import json
from scipy.interpolate import RegularGridInterpolator
import numpy as np
import os
from itertools import product

# 读取数据
def load_data_from_txt(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    data = json.loads(file_content)
    return list(data)

# 创建插值函数
def create_interpolator(data):
    Vol = data[:, 3]
    Tran = data[:, 4]
    Cap = data[:, 5]
    voltages = np.unique(Vol)
    trans = np.unique(Tran)
    cap = np.unique(Cap)
    sort_indices = np.lexsort((Cap, Tran, Vol))
    sorted_data = data[sort_indices]
    value = sorted_data[:,6:8]
    interpolator = RegularGridInterpolator(
        (voltages, trans, cap),
        value.reshape(len(voltages), len(trans), len(cap), 2),
        bounds_error=False,
        fill_value=None
    )
    return interpolator, list(voltages), list(trans), list(cap)


# 主函数
def main(txt_directory, Vol, Tran, Cap):
    all_data = []
    for file_name in os.listdir(txt_directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(txt_directory, file_name)
            data = load_data_from_txt(file_path)
            all_data.append(data)
    data = np.vstack(all_data)
    interpolator, real_vol, real_tran, real_cap = create_interpolator(data)
    interpolated_values = []
    Vol = Vol +real_vol
    Tran = Tran + real_tran
    Cap = Cap + real_cap
    query_points = [list(comb) for comb in product(Vol, Tran, Cap)]
    for point in query_points:
        voltage, trans, cap = point
        interpolated_values.append(interpolator([voltage, trans, cap]))

    return interpolated_values, query_points


# 设定要插值的点
Vol = [0.9]
Tran = [1,1.2]
Cap = [0.6,0.7]
result, query_points = main('/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Dataset/train', Vol, Tran, Cap)

# 提取并保存数据
def save_results_to_txt(results, query_points):
    new_tphl = []
    new_tplh = []
    new_vol = []
    new_tran = []
    new_cap = []
    for i, res in enumerate(results):
        new_tphl.append(round(res[0][0],5))
        new_tplh.append(round(res[0][1],5))
        new_vol.append(query_points[i][0])
        new_tran.append(query_points[i][1])
        new_cap.append(query_points[i][2])
    # print(new_tphl,new_tplh,new_vol,new_tran)
    output_dir = 'output_files'
    os.makedirs(output_dir, exist_ok=True)
    vol_unique = list(set(new_vol))
    for vol_value in vol_unique:
        indices = [i for i, x in enumerate(new_vol) if x == vol_value]
        x = [new_tran[i] for i in indices]
        y = [new_cap[i] for i in indices]
        z1 = [new_tphl[i] for i in indices]
        z2 = [new_tplh[i] for i in indices]
        file_name = f'{output_dir}/AND_Vol_{vol_value}_tphl_r.csv'
        #原版数据x,y,z数列排序输出
        with open(file_name, 'w') as file:
            file.write("Tran, Cap, Tphl\n")
            for xi, yi, zi in zip(x, y, z1):
                file.write(f"{xi}, {yi}, {zi}\n")
        x_unique = sorted(set(x))
        y_unique = sorted(set(y))
        matrix = np.zeros((len(y_unique), len(x_unique)))
        for xi, yi, zi in zip(x, y, z1):
            x_index = x_unique.index(xi)
            y_index = y_unique.index(yi)
            matrix[y_index, x_index] = zi
        file_name = f'{output_dir}/AND_Vol_{vol_value}_tphl.csv'
        #整理数据,x，y为横纵坐标，z为值
        with open(file_name, 'w') as file:
            file.write(',' + ','.join(map(str, x_unique)) + '\n')
            for yi, row in zip(y_unique, matrix):
                file.write(f"{yi}," + ','.join(map(str, row.astype(float))) + '\n')

        file_name = f'{output_dir}/AND_Vol_{vol_value}_tplh_r.csv'
        #原版数据x,y,z数列排序输出
        with open(file_name, 'w') as file:
            file.write("Tran, Cap, Tplh\n")
            for xi, yi, zi in zip(x, y, z2):
                file.write(f"{xi}, {yi}, {zi}\n")
        x_unique = sorted(set(x))
        y_unique = sorted(set(y))
        matrix = np.zeros((len(y_unique), len(x_unique)))
        for xi, yi, zi in zip(x, y, z2):
            x_index = x_unique.index(xi)
            y_index = y_unique.index(yi)
            matrix[y_index, x_index] = zi
        file_name = f'{output_dir}/AND_Vol_{vol_value}_tplh.csv'
        #整理数据,x，y为横纵坐标，z为值
        with open(file_name, 'w') as file:
            file.write(',' + ','.join(map(str, x_unique)) + '\n')
            for yi, row in zip(y_unique, matrix):
                file.write(f"{yi}," + ','.join(map(str, row.astype(float))) + '\n')

save_results_to_txt(result, query_points)
print('Over')