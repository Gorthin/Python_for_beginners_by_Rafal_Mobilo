name = 'Adrian'
age = 34
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name,age,age*daysInYear))

print(message % (name,age,age*daysInYear))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,age*daysInYear))
print('12345678424290 divided by 124234345 is ',12345678424290 // 124234345,'and the rest is',12345678424290 % 124234345)