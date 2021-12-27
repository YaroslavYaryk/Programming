import json
import openpyxl

book = openpyxl.Workbook()
sheet = book.active
sheet['B1'] = 'ID'
sheet['C1'] = 'TITLE'
sheet['D1'] = 'YEAR'
sheet['E1'] = 'RUNTIME'
sheet['F1'] = 'DIRECTOR'
sheet['G1'] = 'PLOT'
sheet['H1'] = 'posterUrl'
sheet['F1'] = 'Genre'



with open('mine.json') as file:
    data = json.load(file)
row = 2
for movies in data["movies"]:
    sheet[row][1].value = movies['id']
    sheet[row][2].value = movies['title']
    sheet[row][3].value = movies['year']
    sheet[row][4].value = movies['runtime']
    sheet[row][5].value = movies['director']
    sheet[row][6].value = movies['plot']
    sheet[row][7].value = movies['posterUrl']
    sheet[row][0].value = movies['GENRES']
    row+=1

for g in data["genres"]:
    sheet[row][0].value = g
    row+=1




book.save('mt_book.xlsx')
book.close()