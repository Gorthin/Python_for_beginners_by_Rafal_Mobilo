min_likes = 500
min_shares = 100
num_likes = 1000
num_shares = 300

if num_likes > min_likes and num_shares > min_shares:
    print('Today w have a 10% salary!!!')
else:
    print('Sorry, we need more likes and shares!')

print('#2')
isPizzaOrdered = True
isDrinkOrdered = True
isWeekend = True

if (isPizzaOrdered or isDrinkOrdered) and not isWeekend:
    print('You have a extra coupon!')
else:
    print('Sorry try again!')

print('#3')
discSize = 100
discUsedSized = 70
fileSize = 40

if (discSize - discUsedSized) > fileSize:
    print('You can be downloaded')
else:
    print('You can\'t be downloaded')

