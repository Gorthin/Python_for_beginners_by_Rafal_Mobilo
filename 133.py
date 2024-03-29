import math
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print(len(inputdata))
print(len(factortable))

if len(inputdata) == len(factortable):
    i = 0
    while i < len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print('minvalue=', minvalue, 'maxvalue=', maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, "\t", inputdata[i], "\t", maxinteger)
        i += 1
    print("OK")
elif len(inputdata) != len(factortable):
    print("inputdata and factortable need to have equal number of elements")

print("===========")

import random

i = 0
while i < len(inputdata):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]
    print('minvalue=', minvalue, 'maxvalue=', maxvalue)

    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger, "\t", inputdata[i], "\t", maxinteger)
    i += 1

print("===========")

from datetime import datetime
print(datetime.today())
print(datetime.today().strftime('%Y-%m-%d'))