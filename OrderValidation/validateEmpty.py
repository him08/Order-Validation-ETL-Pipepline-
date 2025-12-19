


def validateEmpty(rows,products):
    file_is_valid=True
    for row in rows:
        if "" in row[1:] or "" in products[1:]:
            print(f'Empty field in {row}')
            file_is_valid=False
        else:
            print(f'Not Empty')





