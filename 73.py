MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 10
num_shares = 1

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:

    print('GREAT! Today our prizes drop 10% !!!')

elif num_likes <MIN_LIKES:

     print('We still need more likes to start the promotion')

else:

     print('We still need more shares to start the promotion')
print('--------')

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = True

if (isPizzaOrdered  or isBigDrinkOrdered) and not isWeekend:
    print('Kupon na Burgera')
elif isWeekend:
    print('Promocja wylacznie poza weekendem')
else:
    print('Nalezy zamowic pizze lub napoj')
