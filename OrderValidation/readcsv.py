import os

def readFiles(file_path):
    all_rows = []

    with open(file_path, "r") as f:
        lines = f.readlines()

        # skip header
        for line in lines[1:]:
            line = line.strip()
            if line == "":
                continue
            all_rows.append(line.split(","))

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


