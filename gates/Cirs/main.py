import subprocess
import os

def delete_non_python_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and not filename.endswith('.py'):
            os.remove(file_path)

delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Cirs/generated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Cirs/simulated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Cirs/results')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Cirs/results/pivot')


scripts = [ '/data/yaohuihan/Research/STA_Modeling/gates/Cirs/generated/generate_hspice.py', 
            '/data/yaohuihan/Research/STA_Modeling/gates/Cirs/simulated/run_hspice.py', 
            '/data/yaohuihan/Research/STA_Modeling/gates/Cirs/results/post_process1.py', 
            '/data/yaohuihan/Research/STA_Modeling/gates/Cirs/results/post_process2.py',
            '/data/yaohuihan/Research/STA_Modeling/gates/Cirs/results/post_process3.py']

for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        break
