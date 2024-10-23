import sys
import ast

vol = 0.7

vol_pre = [0, 0.03, 0.1, 0.158744, 0.221271, 0.279374, 0.333513, 0.3841, 0.437223, 0.533203, 0.58153, 0.626864, 0.717883, 0.806555, 0.9, 0.958983, 1]  # 电压百分比

trans_time = {
    '5': [0, 0.375, 0.625, 0.84375, 1.09375, 1.34375, 1.59375, 1.84375, 2.125, 2.6875, 3, 3.3125, 4, 4.75, 5.625, 6.21875, 6.65625]
}

def generate_trans_time(input, norm):
    factor = input / 5
    the_norm = norm['5']
    new_trans_time = [i * factor for i in the_norm]
    return new_trans_time

def gen_interpolation_data(x, y, num_points=30, method='linear'):
    """
    method = ['linear', 'quadratic', 'cubic']
    """
    import numpy as np
    from scipy.interpolate import interp1d

    interx_np = np.array(x)
    intery_np = np.array(y)
    interpolator = interp1d(interx_np, intery_np, kind=method)
    new_x = np.linspace(np.min(interx_np), np.max(interx_np), num_points)
    new_y = interpolator(new_x)
    return new_x.tolist(), new_y.tolist()

def plt_waveform(key, pwl_value):
    import matplotlib.pyplot as plt
    time_data = [float(pwl_value[i][:-1]) for i in range(0, len(pwl_value), 2)]
    voltage_data = [float(pwl_value[i][:-1]) for i in range(1, len(pwl_value), 2)]
    # 绘制波形
    plt.figure()
    plt.plot(time_data, voltage_data, label=f"Transition {key}p")
    plt.xlabel('Time (p)')
    plt.ylabel('Voltage (V)')
    plt.title(f'Voltage vs Time - Transition {key}p')
    plt.grid(True)
    plt.legend()

    # 保存波形图
    plt.savefig(f"waveform_driver_{key}p.png")
    plt.close()


def generate_rise_values(time_values, vol_pre):
    rise_values = []
    rise_end = 0.0
    for p_vol, t in zip(vol_pre, time_values):
        rise_values.append(f"{t}p")
        rise_values.append(f"{vol * p_vol:.7f}V")
        rise_end = t
    rise_end += 1000
    rise_values.extend([f"{rise_end}p", "0.7000000V"])
    return rise_values, rise_end


def generate_fall_values(rise_end, time_values, vol_pre):
    # Cell_rise MAPE: 1.12%
    # Cell_fall MAPE: 0.73%
    # 这个的理解为：
    # vol对应的变化为 1-index2，time即顺序(与rise的一致，rise基准点为0，这里基准点为rise_end)
    fall_values = []
    rise_end2 = rise_end
    for p_vol, t in zip(vol_pre, time_values):
        rise_end2 += t
        fall_values.append(f"{rise_end + t}p")
        fall_values.append(f"{vol * (1 - p_vol):.7f}V")
    rise_end2 += 1000
    fall_values.extend([f"{rise_end2}p", "0.0000000V"])
    return fall_values

def func (input_key):
    trans_time = {
        '5': [0, 0.375, 0.625, 0.84375, 1.09375, 1.34375, 1.59375, 1.84375, 2.125, 2.6875, 3, 3.3125, 4, 4.75, 5.625,
              6.21875, 6.65625]
    }
    for i in input_key:
        key = int(i)
        name = str(key)
        if name not in trans_time:
            trans_time[name] = generate_trans_time(key,trans_time)

    # 0 0V 0.375p 0.021V 0.625p 0.07V
    # time, vol
    PWL = []
    for trans_index, time_values in trans_time.items():
        pwl_value = []
        new_time, new_vol = gen_interpolation_data(x=time_values, y=vol_pre, num_points=50, method='cubic')
        # 生成 上升波形
        rise_values, rise_end = generate_rise_values(new_time, new_vol)
        pwl_value.extend(rise_values)
        # 生成 下降波形
        fall_values = generate_fall_values(rise_end, new_time, new_vol)
        pwl_value.extend(fall_values)
        PWL.append(pwl_value)

    # 写入文件
    for pwl, trans_index in zip(PWL, trans_time.keys()):
        pwl_str = ' '.join(pwl)
        file_name = f'/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/models/waveform/driver_{trans_index}p'
        with open(file_name, 'w') as f:
            f.write(f'VIN_A an 0 PWL({pwl_str})')
            print("\033[1;32mWaveform Generator\033[0m: Loaded "+file_name)

if __name__ == "__main__":
    input_list = ast.literal_eval(sys.argv[1])  # 将字符串转换为列表
    func(input_list)