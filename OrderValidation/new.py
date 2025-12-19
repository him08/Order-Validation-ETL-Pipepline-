
from readcsv import readFiles
from validateCity import validateCity
from validateEmpty import validateEmpty
from validateProductId import validateProductId
from validateTotalSalesAmount import validateAmount
from validateDate import validateDate

rows1=readFiles('incoming_files/20251712')
rows2=readFiles('incoming_files/20251812')
products = []
with open('product_master.csv', 'r') as f:
    lines = f.readlines()
    header = lines[0]
    data_lines=lines[1:]
    for row in data_lines:
        row=row.strip()
        columns=row.split(",")
        products.append(columns)

print(rows1)
print(rows2)
print(products)
# *****MAKING A PRODUCT DICTIONARY WITH ID AND PRICE----------
product_dict={}
for product in products:
    product_id=product[0]
    product_price=product[3]
    product_dict[product_id]=product_price

# MAIN FUNC TO CALL ALL FUNCS
def validate_file(rows, product_dict):
    id_ok     = validateProductId(rows, product_dict)
    city_ok   = validateCity(rows)
    empty_ok  = validateEmpty(rows,products)
    amount_ok = validateAmount(rows, product_dict)
    date_ok   = validateDate(rows)

    return id_ok and city_ok and empty_ok and amount_ok and date_ok

rows1_ok = validate_file(rows1, product_dict)
rows2_ok = validate_file(rows2, product_dict)

print("rows1 final status:", rows1_ok)
print("rows2 final status:", rows2_ok)

