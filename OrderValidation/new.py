import os
from readcsv import readFiles
from validateCity import validateCity
from validateEmpty import validateEmpty
from validateProductId import validateProductId
from validateTotalSalesAmount import validateAmount
from validateDate import validateDate


# LOAD PRODUCT MASTER

products = []
with open("product_master.csv", "r") as f:
    lines = f.readlines()
    header = lines[0]
    for row in lines[1:]:
        products.append(row.strip().split(","))

product_dict = {}
for product in products:
    product_dict[product[0]] = int(product[3])


# FILE LEVEL VALIDATION

def validate_file(rows):
    id_ok     = validateProductId(rows, product_dict)
    city_ok   = validateCity(rows)
    empty_ok  = validateEmpty(rows,products)
    amount_ok = validateAmount(rows, product_dict)
    date_ok   = validateDate(rows)

    return id_ok and city_ok and empty_ok and amount_ok and date_ok

# MAIN PIPELINE

INCOMING_DIR = "incoming_files"

for date_folder in os.listdir(INCOMING_DIR):
    date_path = os.path.join(INCOMING_DIR, date_folder)

    if not os.path.isdir(date_path):
        continue

    for file_name in os.listdir(date_path):
        if not file_name.endswith(".csv"):
            continue

        file_path = os.path.join(date_path, file_name)
        print("\nProcessing:", file_path)

        # READ ONE FILE
        rows = readFiles(file_path)

        # VALIDATE FILE
        file_ok = validate_file(rows)

        if not file_ok:
            # WRITE TO REJECTED FILES
            rejected_dir = os.path.join("rejected_files", date_folder)
            os.makedirs(rejected_dir, exist_ok=True)

            rejected_file = os.path.join(rejected_dir, file_name)

            with open(rejected_file, "w") as f:
                f.write(header)
                for row in rows:
                    f.write(",".join(row) + "\n")

            print("Rejected:", rejected_file)
        else:
            success_dir=os.path.join('success_files',date_folder)
            os.makedirs(success_dir, exist_ok=True)
            success_file = os.path.join(success_dir, file_name)
            with open(success_file, "w") as f:
                f.write(header)
                for row in rows:
                    f.write(",".join(row) + "\n")

            print("File passed validation:", file_name)



