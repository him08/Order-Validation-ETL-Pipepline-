
def validateCity(rows):
   file_is_valid=True
   for row in rows:
       city=row[4]
       if city=='Mumbai' or city=='Bangalore':
           print(f'valid city {city}')
       else:
           print(f'not valid {city}')
           file_is_valid=False
   return file_is_valid




