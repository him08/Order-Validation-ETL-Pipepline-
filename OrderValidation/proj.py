import os
folder_path="incoming_files/20251712"
files=os.listdir(folder_path)
print(files)

for file_name in files:
    file_path=os.path.join(folder_path,file_name)
    with open(file_path,'r') as f:
        print(f.read())

folder_path2="incoming_files/20251812"
# os.remove("incoming_files/20251712/.DS_Store")

files=os.listdir(folder_path2)
print(files)
# os.remove("incoming_files/20251812/.DS_Store")
for file_name in files:
    file_path2=os.path.join(folder_path2,file_name)
    with open(file_path2,'r') as f:
        print(f.read())

