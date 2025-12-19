import datetime



today=datetime.date.today()
print(today)

def validateDate(rows):
    file_is_valid=True
    for row in rows:
        order_date=row[3]
        today = datetime.date.today().isoformat()
        if order_date > today:
            print(f'not valid {order_date}')
            file_is_valid = False
        else:
            print('valid')

    return file_is_valid



