
from new import rows1,rows2,products

def validateEmpty(rows,products):

    for row in rows:
        if "" in row[1:] or "" in products[1:]:
            print("Empty")
        else:
            print("Not Empty")

validateEmpty(rows1,products)
validateEmpty(rows2,products)



