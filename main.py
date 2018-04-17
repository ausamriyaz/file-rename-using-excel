import os
from xlrd import open_workbook

data = []


def appendTolist():
    book = open_workbook(input('Enter excel file path with file name and extension: '))

    sheet = book.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        temp = str(sheet.row_values(row, 0))

        data.append(temp[2:-2])


def renameFiles():
    count=0
    os.chdir(input("directory of the files to be renamed: "))
    all_file_in_dir = (os.listdir(os.getcwd()))
    i = 0
    for x in all_file_in_dir:
        if count==0:
            os.rename(x, data[i] + ".txt")
            i += 1
            if len(data)==i:
                count+=1
                i=0
        else:
            os.rename(x, data[i]+"("+str(count)+")" + ".txt")
            i += 1
            if len(data) == i:
                count += 1
                i = 0





appendTolist()
renameFiles()

