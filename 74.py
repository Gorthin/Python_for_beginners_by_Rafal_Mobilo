min_likes = 500
min_shares = 100
num_likes = 100
num_shares = 20

if num_likes >= min_likes and num_shares >= min_shares:
    print('Today w have a 10% salary!!!')
else:
    if num_likes < min_likes:
        print('Sorry, we need more likes!')
    else:
        print('We need more shares')

if num_likes >= min_likes and num_shares >= min_shares:
    print('Today w have a 10% salary!!!')
elif num_likes < min_likes:
    print('Sorry, we need more likes!')
else:
    print('We need more shares')

print('#2')

isPizzaOrdered = True
isDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered or isDrinkOrdered) and not isWeekend:
    print('You have a extra coupon!')
else:
    if not isPizzaOrdered:
        print('Sorry you must buy a pizza!')
    else:
        if not isDrinkOrdered:
            print('You must buy a big drink!')
        else:
            if isWeekend:
                print('Sorry we have a weekend')

if (isPizzaOrdered or isDrinkOrdered) and not isWeekend:
    print('You have a extra coupon!')
elif isWeekend:
    print('Sorry we have a weekend')
else:
    print('You need to order pizza or drink')