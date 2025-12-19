errors=[]
def validateAmount(rows,product_dict,errors):
    file_is_valid=True
    for row in rows:
      product_id=row[1]
      if row[2] == "":
          print(f"Invalid quantity for order {row[0]}")
          continue
      order_total_sales = int(row[5])
      order_quantity = int(row[2])
      if product_id not in product_dict:
          print(f"Invalid product for order {row[0]}")
          continue
      expected_amount = product_dict[product_id] * order_quantity
      if expected_amount==order_total_sales:
        print(f'valid sales amount{product_dict[product_id]} ')

      else:
        print(f'not valid {product_dict[product_id]} ')
        errors.append(row+['total sales mismatch'])
        file_is_valid=False

    return file_is_valid



