vol = 0.7

vol_pre = [0, 0.03, 0.1, 0.158744, 0.221271, 0.279374, 0.333513, 0.3841, 0.437223, 0.533203, 0.58153, 0.626864, 0.717883, 0.806555, 0.9, 0.958983, 1]  # 电压百分比

trans_time = {
    '5': [0, 0.375, 0.625, 0.84375, 1.09375, 1.34375, 1.59375, 1.84375, 2.125, 2.6875, 3, 3.3125, 4, 4.75, 5.625, 6.21875, 6.65625],
    '10': [0, 0.75, 1.25, 1.6875, 2.1875, 2.6875, 3.1875, 3.6875, 4.25, 5.375, 6, 6.625, 8, 9.5, 11.25, 12.4375, 13.3125],
    '20': [0, 1.5, 2.5, 3.375, 4.375, 5.375, 6.375, 7.375, 8.5, 10.75, 12, 13.25, 16, 19, 22.5, 24.875, 26.625],
    '40': [0, 3, 5, 6.75, 8.75, 10.75, 12.75, 14.75, 17, 21.5, 24, 26.5, 32, 38, 45, 49.75, 53.25],
    '80': [0, 6, 10, 13.5, 17.5, 21.5, 25.5, 29.5, 34, 43, 48, 53, 64, 76, 90, 99.5, 106.5],
    '160': [0, 12, 20, 27, 35, 43, 51, 59, 68, 86, 96, 106, 128, 152, 180, 199, 213],
    '320': [0, 24, 40, 54, 70, 86, 102, 118, 136, 172, 192, 212, 256, 304, 360, 398, 426]
}


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


def generate_rise_values(time_values):
    rise_values = []
    rise_end = 0.0
    for p_vol, t in zip(vol_pre, time_values):
        rise_values.append(f"{t}p")
        rise_values.append(f"{vol * p_vol:.7f}V")
        rise_end = t
    rise_end += 1000
    rise_values.extend([f"{rise_end}p", "0.7000000V"])
    return rise_values, rise_end


def generate_fall_values(rise_end, time_values):
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


# 0 0V 0.375p 0.021V 0.625p 0.07V
# time, vol
PWL = []
for trans_index, time_values in trans_time.items():
    pwl_value = []
    # 生成 上升波形
    rise_values, rise_end = generate_rise_values(time_values)
    pwl_value.extend(rise_values)
    # 生成 下降波形
    fall_values = generate_fall_values(rise_end, time_values)
    pwl_value.extend(fall_values)
    PWL.append(pwl_value)

# 写入文件
for pwl, trans_index in zip(PWL, trans_time.keys()):
    pwl_str = ' '.join(pwl)
    with open(f'waveform/driver_{trans_index}p', 'w') as f:
        f.write(f'VIN_A an 0 PWL({pwl_str})')
