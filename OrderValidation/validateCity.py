from new import rows1,rows2


def validateCity(rows):
   for row in rows:
       city=row[4]
       if city=='Mumbai' or city=='Banglore':
           print('valid')
       else:
           print('not valid')


validateCity(rows1)
validateCity(rows2)