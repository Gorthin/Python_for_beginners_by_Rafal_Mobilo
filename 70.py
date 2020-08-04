# zad 1

MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 1000
num_shares = 123

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print("Obniżka cen o 10%")
else:
    print("Brak obniżki cen o 10%, za mało lajkow i udostepnien")

# zad 2

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = True

if (isPizzaOrdered  or isBigDrinkOrdered) and not isWeekend:
    print('Kupon na Burgera')
else:
    print('Brak kuponu')

# zad 3

diskSize = 140  # wielkosc dysku  w GB
diskSizeUsed = 111 # ilosc zajetego miesca na dysku w GB
fileSize = 12 # wielkosc pobieranego pliku

if fileSize < (diskSize - diskSizeUsed):
    print('File can be downloaded')
else:
    print('File can not be downloaded')
