import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
#print(time.localtime(time.clock()))

import calendar

print(calendar.month(2020,3,w=5,l=2))
print(calendar.month(2020,3))
print(calendar.weekday(1988,8,18))
print(calendar.setfirstweekday(6))
print(calendar.month(2017,9))
print(calendar.weekday(1988,8,18))
print(calendar.leapdays(2000,2020))
print(calendar.isleap(2020))
print(calendar.calendar(2020))
