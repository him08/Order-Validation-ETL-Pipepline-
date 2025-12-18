from new import rows1, product_dict
from new import rows2

print(rows1)
print(product_dict)
def validateProductId(rows,productId):
    for row in rows:
        order_product_id=row[1]
        if order_product_id in product_dict.keys():
            print('Valid product id')
            return True
        else:
            print('Invalid product id')
            return False


validateProductId(rows1,product_dict)
validateProductId(rows2,product_dict)

