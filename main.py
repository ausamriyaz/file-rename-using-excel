import collections
import os

import errno
from xlrd import open_workbook

data = []
data1 = []


def appendTolist():
    book = open_workbook(input('Enter excel file path with file name and extension: '))

    sheet = book.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        temp = str(sheet.row_values(row, 0))

        data.append(temp[2:-2])



def renameFiles():
    count = 0
    dire = input("directory of the files to be renamed: ")
    initRename(dire)
    os.chdir(dire)
    all_file_in_dir = (os.listdir(os.getcwd()))
    i = 0
    for x in all_file_in_dir:
        try:
            if count == 0:

                os.rename(x, data1[i] + ".txt")
                i += 1
                if len(data1) == i:
                    count += 1
                    i = 0

            else:
                os.rename(x, data1[i] + "(" + str(count) + ")" + ".txt")
                i += 1
                if len(data1) == i:
                    count += 1
                    i = 0
        except OSError as e:
            if e.errno == errno.EEXIST:
                i += 1
                os.rename(x, data1[i] + ".txt")
            else:
                raise


def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output



def initRename(dire):
    os.chdir(dire)
    all_file_in_dir = (os.listdir(os.getcwd()))
    i = 0
    for x in all_file_in_dir:
        os.rename(x, "1" +"("+str(i)+")" ".txt")
        i += 1




appendTolist()
data1 = remove_duplicates(data)
renameFiles()


##C:\Users\ausam\Downloads\Untitled spreadsheet.xlsx
##J:\movies\sample