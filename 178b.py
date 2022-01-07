#!/usr/bin/python3


#2
import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("Enter correct path")
webaddress2 = []
with open(filename, 'r') as file:
    for line in filename:
        line = line.replace('\n', '')
        webaddress2.append(line)
        print(line)
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')