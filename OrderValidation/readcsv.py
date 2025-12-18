import os

def readFiles(folder_path):
    files = os.listdir(folder_path)
    all_rows = []
    for file_name in files:
        if not file_name.endswith(".csv"):
            continue

        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "r") as f:
            print(f"\n--- Reading {file_name} ---")
            lines=f.readlines()
            header =lines[0]
            data_lines=lines[1:]
            for line in data_lines:
                line=line.strip()
                if line=="":
                    continue
                columns=line.split(",")
                all_rows.append(columns)
        return all_rows

# folder_path2="incoming_files/20251812"
# os.remove("incoming_files/20251712/.DS_Store")

# files=os.listdir(folder_path2)
# print(files)
# os.remove("incoming_files/20251812/.DS_Store")
# for file_name in files:
#     file_path2=os.path.join(folder_path2,file_name)
#     with open(file_path2,'r') as f:
#         print(f.read())

