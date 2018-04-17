import collections
import os

import errno
import random
import string

from xlrd import open_workbook

data = []
data1 = []

'''
extract data from the excel sheet
'''


def appendTolist():
    book = open_workbook(
        input('Enter excel file path with file name and extension: '))  ##opens the whole file in to the variable book

    sheet = book.sheet_by_index(0)  ##extract the 0th row

    for row in range(1, sheet.nrows):  ##loops through all the rows
        temp = str(sheet.row_values(row, 0))  ##gets the value of the row and converts to stringeg: '[rowdata]'

        data.append(
            temp[2:-2])  ##removes the brackets and quotation marks on the row value extracted and appends to the list


'''
renames all the files
'''

def renameFiles():
    count = 0
    dire = input("directory of the files to be renamed: ")##get directory name
    initRename(dire)##rename all the fimes to random charecters to make sure there are no duplicate file names
    os.chdir(dire)
    all_file_in_dir = (os.listdir(os.getcwd()))##assign all the names to all_file_in_dir
    i = 0
    for x in all_file_in_dir:##loop through a all_file_in_dir
        try:
            if count == 0:
                extension = x.split(".")[-1]##get extension

                os.rename(x, data1[i] + "." + extension)##rename
                i += 1
                if len(data1) == i:##check if the number of rows are reached
                    count += 1
                    i = 0

            else:
                extension = x.split(".")[-1]

                os.rename(x, data1[i] + "(" + str(count) + ")" + "." + extension)
                i += 1
                if len(data1) == i:
                    count += 1
                    i = 0
        except OSError as e:##file already exist handled
            if e.errno == errno.EEXIST:
                i += 1

                extension = x.split(".")[-1]

                os.rename(x, data1[i] + "(" + str(count) + ")" + "." + extension)
                i += 1
                if len(data1) == i:
                    count += 1
                    i = 0
            else:
                raise

'''
remove duplicate items from the excel sheet
'''
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

'''
rename all the fimes to random charecters to make sure there are no duplicate file names
'''
def initRename(dire):
    os.chdir(dire)
    all_file_in_dir = (os.listdir(os.getcwd()))
    i = 0
    for x in all_file_in_dir:
        extension = x.split(".")[-1]
        os.rename(x, randCharGenerator() + "." + extension)
        i += 1

'''
random charecter generation
'''
def randCharGenerator(size=18, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


appendTolist()
data1 = remove_duplicates(data)
renameFiles()

##C:\Users\ausam\Downloads\Untitled spreadsheet.xlsx
##J:\movies\sample
