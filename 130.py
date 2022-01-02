import time
print(time.time())
print(time.localtime(time.time()))
import calendar
print(calendar.month(2022, 4, w=3, l=1))
calendar.setfirstweekday(6)
print(calendar.month(2022, 4, w=3, l=1))
print(calendar.isleap(2000))
calendar.setfirstweekday(0)
print(calendar.calendar(2022))