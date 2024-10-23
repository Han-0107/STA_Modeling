import os
import re
import csv
import glob

def get_binary_code(logic_gate):
    # 定义操作符到三位二进制码的映射
    gate_to_binary = {
        'and': '001',
        'nand': '010',
        'nor': '011',
        'not': '100',
        'or': '101',
        'xnor': '110',
        'xor': '111'
    }
    return gate_to_binary.get(logic_gate, '000')

def get_code_from_list(input_list):
    if not input_list:
        return '000'
    first_item = input_list[0]
    return get_binary_code(first_item)

def extract_data_to_csv(file_path, csv_writer):
    filename = os.path.basename(file_path)
    second_value = None
    third_value = None
    fourth_value = None
    if 'VOL_' in filename:
        match = re.search(r'VOL_(\d+\.\d+)', filename)
        if match:
            second_value = match.group(1)
    if 'Trans_' in filename:
        match = re.search(r'Trans_(\d+(\.\d+)?)', filename)
        if match:
            third_value = match.group(1)
    if 'Cap_' in filename:
        match = re.search(r'Cap_(\d+\.\d+)', filename)
        if match:
            fourth_value = match.group(1)
    
    with open(file_path, "r") as file:
        data = file.read()
    lines = data.splitlines()
    line = lines[3].strip()
    line2 = lines[1].strip()
    # 允许匹配整数、浮点数、科学计数法和非数字字符串
    pattern = r'\S+'
    matches = re.findall(pattern, line)
    pattern2 = r'\b(and|nand|nor|not|or|xnor|xor)\b'
    matches2 = re.findall(pattern2, line2)
    if len(matches) >= 2:
        first_match = round(float(matches[0]) * (10 ** 9), 5)
        second_match = round(float(matches[1]) * (10 ** 9), 5)
        first_value = get_code_from_list(matches2)
        csv_writer.writerow([first_value, second_value, third_value, fourth_value, first_match, second_match])
    else:
        print(f"Less than two matches found in {file_path}")
        first_value = get_code_from_list(matches2)
        csv_writer.writerow([first_value, second_value, third_value, fourth_value, '', ''])

def process_files(folder_path, output_directory):
    files = glob.glob(os.path.join(folder_path, "*.mt0"))
    if not files:
        print(f"No .mt0 files found in {folder_path}")
        return
    
    # Specify the path for the CSV file in the output directory
    csv_file = os.path.join(output_directory, "All_data.csv")
    with open(csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Gate", "VOL", "Trans", "Cap", "Tphl", "Tplh"])
        for file_path in files:
            extract_data_to_csv(file_path, csv_writer)
    
    print(f"\033[1;32mPost Process 1\033[0m: All data extracted from {len(files)} files saved to {csv_file}")

if __name__ == "__main__":
    folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/simulated'
    process_files(folder_path, '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot')
