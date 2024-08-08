import os
import re
import csv
import glob

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
        match = re.search(r'Trans_(\d+\.\d+)', filename)
        if match:
            third_value = match.group(1)
    if 'Cap_' in filename:
        match = re.search(r'Cap_(\d+\.\d+)', filename)
        if match:
            fourth_value = match.group(1)
    
    with open(file_path, "r") as file:
        data = file.read()
    pattern = r"\d+\.\d+e-\d+"
    matches = re.findall(pattern, data)
    if len(matches) >= 2:
        first_match = matches[0]
        second_match = matches[1]
        csv_writer.writerow([first_match, second_match, second_value, third_value, fourth_value])
    else:
        print(f"Less than two matches found in {file_path}")
        csv_writer.writerow(['', second_value, third_value, fourth_value])

def process_files(folder_path, output_directory):
    files = glob.glob(os.path.join(folder_path, "*.mt0"))
    if not files:
        print(f"No .mt0 files found in {folder_path}")
        return
    
    # Specify the path for the CSV file in the output directory
    csv_file = os.path.join(output_directory, "All_data.csv")
    with open(csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Tphl", "Tplh", "VOL", "Trans", "Cap"])
        for file_path in files:
            extract_data_to_csv(file_path, csv_writer)
    
    print(f"Data extracted from {len(files)} files saved to {csv_file}")

if __name__ == "__main__":
    folder_path = '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/simulated'
    process_files(folder_path, '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results')
