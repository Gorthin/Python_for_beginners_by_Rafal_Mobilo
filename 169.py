#!/usr/bin/python3

import os, time

dir = input("Give me path!")
if os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:
    file = input("Give me a filename: ")
    path = os.path.join(dir, file)

    if os.path.exists(path):
        print("File do not exists!")
    else:
        print('displaying properties of file %s' % path)

        print('Last modified date', time.localtime(os.path.getmtime(path)))
        print('Size in bytes', os.path.getsize(path))

        print('Current directory is: ', os.getcwd())
        print('Relative path to the file is', os.path.relpath(path))