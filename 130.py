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
