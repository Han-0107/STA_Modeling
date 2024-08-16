import csv
import os


def process_file(file_path):
    index1 = []
    index2 = []
    values = []

    # Read the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        index1 = header[1:]  # Header columns (excluding the first column)

        # Read rows and prepare data
        for row in reader:
            index2_value = float(row[0]) * 0.6  # Process the first column
            index2.append(f'{index2_value:.2f}')
            values.append(row[1:])  # Collect all the values

    # Transpose the values
    transposed_values = list(zip(*values))

    # Prepare the result dictionary
    result = {
        'index_1': ', '.join(index1),
        'index_2': ', '.join(index2),
        'values': transposed_values
    }
    return result


def save_data(file_path, data):
    new_file_path = file_path.replace('.csv', '.lib')

    with open(new_file_path, 'w') as file:
        file.write('index_1 ("{}");\n'.format(data['index_1']))
        file.write('index_2 ("{}");\n'.format(data['index_2']))
        file.write('values ( \\\n')

        # Write transposed values
        for index, row in enumerate(data['values']):
            row_data = ', '.join(row)
            if index == len(data['values']) - 1:
                file.write('    "{}");\n'.format(row_data))
            else:
                file.write('    "{}", \\\n'.format(row_data))
        file.write('\n')


def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv') and 'pivot' not in filename and 'data' not in filename:  # Exclude files with 'pivot'
            file_path = os.path.join(folder_path, filename)
            data = process_file(file_path)
            save_data(file_path, data)


folder_path = '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results'
process_folder(folder_path)
print('LIB files have been generated')
