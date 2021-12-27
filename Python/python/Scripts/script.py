import openpyxl

book = openpyxl.open('data.xlsx', read_only=True)
sheet = book.active
print(sheet)
