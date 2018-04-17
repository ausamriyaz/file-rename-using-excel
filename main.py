from xlrd import open_workbook

book = open_workbook(input('Enter file path with file name and extension: '))

sheet = book.sheet_by_index(0)

data = []


def cutit(s, n):
    return s[n:]


for row in range(1, 100):
    temp = str(sheet.row_values(row, 0))

    data.append(temp[2:-2])

print(data)

##C:\Users\ausam\Downloads\Untitled spreadsheet.xlsx
