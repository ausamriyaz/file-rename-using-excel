from xlrd import open_workbook

data = []


def appendTolist():
    book = open_workbook(input('Enter file path with file name and extension: '))

    sheet = book.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        temp = str(sheet.row_values(row, 0))

        data.append(temp[2:-2])


appendTolist()

print(data)

##C:\Users\ausam\Downloads\Untitled spreadsheet.xlsx
