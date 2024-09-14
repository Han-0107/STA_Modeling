import os
import shutil

def copy_files(train_voltages, test_voltages, source_dir='.'):
    train_dir = os.path.join(source_dir, 'train')
    test_dir = os.path.join(source_dir, 'test')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    voltage_status = {voltage: False for voltage in train_voltages + test_voltages}

    for filename in os.listdir(source_dir):
        if filename.startswith('AND_Vol_') and filename.endswith('.txt'):
            try:
                voltage = float(filename.split('_')[2].replace('.txt', ''))

                if voltage in train_voltages:
                    shutil.copy(os.path.join(source_dir, filename), os.path.join(train_dir, filename))
                    print(f"Copied {filename} to train folder.")
                    voltage_status[voltage] = True  
                elif voltage in test_voltages:
                    shutil.copy(os.path.join(source_dir, filename), os.path.join(test_dir, filename))
                    print(f"Copied {filename} to test folder.")
                    voltage_status[voltage] = True  
                else:
                    print(f"{filename} does not match any train or test voltage.")

            except ValueError:
                print(f"Error extracting voltage from {filename}. Skipping this file.")

    for voltage, found in voltage_status.items():
        if not found:
            print(f"Warning: No file found for voltage {voltage}.")

if __name__ == "__main__":
    train_voltages = [0.9, 1.2, 1.5]
    test_voltages = [1.0, 1.3] 

    source_dir = '.'
    copy_files(train_voltages, test_voltages, source_dir)
