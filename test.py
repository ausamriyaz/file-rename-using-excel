import os
import random
import string


def initRename(dire):
    os.chdir(dire)
    all_file_in_dir = (os.listdir(os.getcwd()))
    i = 0
    for x in all_file_in_dir:
        extension = x.split(".")[-1]
        os.rename(x, randCharGenerator()+ "."+randCharGenerator())
        i += 1


def randCharGenerator(size=18, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



initRename('J:\movies\sample')