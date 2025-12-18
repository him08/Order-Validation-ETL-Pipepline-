
from readcsv import readFiles

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





