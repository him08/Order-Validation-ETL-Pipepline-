

def validateProductId(rows,product_dict):
    file_is_valid=True
    for row in rows:
        order_product_id=row[1]
        if order_product_id in product_dict.keys():
            print(f'Valid product id {order_product_id}')
        else:
            print(f'Invalid product id {order_product_id}')
            file_is_valid=False
    return file_is_valid



