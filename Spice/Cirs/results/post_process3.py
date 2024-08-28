import csv
import os

source_folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/csv'
lib_folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/lib'
os.makedirs(lib_folder_path, exist_ok=True)

def process_file(file_path):
    index1 = []
    index2 = []
    values = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        index1 = header[1:]
        for row in reader:
            index2_value = float(row[0]) * 0.6  # Process the first column
            index2.append(f'{index2_value:.2f}')
            values.append(row[1:])
    transposed_values = list(zip(*values))
    result = {
        'index_1': ', '.join(index1),
        'index_2': ', '.join(index2),
        'values': transposed_values
    }
    return result

def save_data(file_path, data, output_folder):
    base_filename = os.path.basename(file_path)
    new_filename = base_filename.replace('.csv', '.lib')
    new_file_path = os.path.join(output_folder, new_filename)

    with open(new_file_path, 'w') as file:
        file.write('index_1 ("{}");\n'.format(data['index_1']))
        file.write('index_2 ("{}");\n'.format(data['index_2']))
        file.write('values ( \\\n')

        for index, row in enumerate(data['values']):
            row_data = ', '.join(row)
            if index == len(data['values']) - 1:
                file.write('    "{}");\n'.format(row_data))
            else:
                file.write('    "{}", \\\n'.format(row_data))
        file.write('\n')

def process_folder(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv') and 'Pivot' not in filename and 'data' not in filename:
            file_path = os.path.join(folder_path, filename)
            data = process_file(file_path)
            save_data(file_path, data, output_folder)

process_folder(source_folder_path, lib_folder_path)
print('\033[1;32mPost Process 3\033[0m: LIB files have been generated and saved to', lib_folder_path)
