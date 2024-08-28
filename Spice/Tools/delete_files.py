import os

def delete_non_python_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and not filename.endswith('.py'):
            os.remove(file_path)

delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/generated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/simulated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/csv')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/lib')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot')
