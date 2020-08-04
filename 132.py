inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math

len(inputdata)
len(factortable)

if len(inputdata) == len(factortable):
    i = 0
    while i < len(inputdata):
        minvalue = inputdata[i]-factortable[i]*inputdata[i]
        maxvalue = inputdata[i]+factortable[i]*inputdata[i]
        i+=1
    print(minvalue,maxvalue)

    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger,maxinteger)
else:
    print("inputdata and factorable need to have equal number of elements")
print('============')

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

print('=========')

import datetime

print(datetime.MINYEAR, datetime.MAXYEAR)
print('==========')
d1 = datetime.timedelta(days=1, hours=2,minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2,minutes=-3)
print(d2)

print(d1+d2)
print('==========')
print(datetime.date.today())

print('==========')

today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print(today)
print(daysToPay)
print(today+daysToPay)
print('==========')


endOfWorld = datetime.date.max
print(endOfWorld)
print(endOfWorld.weekday())

print('==========')

bornDate = datetime.date(2000,8,15)
today = datetime.date.today()
print(today-bornDate)

print('==========')

print("%now", datetime.datetime.now())
print("%today",datetime.datetime.today())
print("%uctnow",datetime.datetime.utcnow())
print("%week day",datetime.datetime.today().weekday())



print('====')

print("%a",datetime.datetime.now().strftime("%a"))
print("%A",datetime.datetime.now().strftime("%A"))
print("%w",datetime.datetime.now().strftime("%w"))
print("%a","%A","%w",datetime.datetime.now().strftime("%a" "%A" "%w"))
print("%a","%A","%w",datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))


