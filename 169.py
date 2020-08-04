import os

fileIsOk = False

while not fileIsOk:

    filename = input('Enter path to result file: ')

    if os.path.isfile(filename):
        break
    else:
        print("File name is not correct, try again")

print("The results file is %s" % (filename))
