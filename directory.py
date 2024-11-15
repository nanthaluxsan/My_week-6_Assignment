import os

# Specify the directory you want to scan
directory = "D:\study_further\Senzemate\week_6\Week6_assignment\Financial_data"

# Get a list of all folders in the directory
folders = [
    os.path.join(directory, name)
    for name in os.listdir(directory)
    if os.path.isdir(os.path.join(directory, name))
]

# Print folder paths
for folder in folders:
    print(folder)
