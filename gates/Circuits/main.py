import subprocess
import os

def delete_non_python_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and not filename.endswith('.py'):
            os.remove(file_path)

delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Circuits/generated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Circuits/simulated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results/pivot')


scripts = [ '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/generated/generate_hspice.py', 
            '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/simulated/run_hspice.py', 
            '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results/post_process1.py', 
            '/data/yaohuihan/Research/STA_Modeling/gates/Circuits/results/post_process2.py']

for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        break

print('Simulate successfully!')
