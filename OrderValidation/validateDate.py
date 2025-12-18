import datetime
from new import rows1,rows2


today=datetime.date.today()
print(today)

def validateDate(rows):
    for row in rows:
        order_date=row[3]
        today = datetime.date.today().isoformat()
        if order_date > today:
            print('not valid')
        else:
            print('valid')

validateDate(rows1)
validateDate(rows2)


