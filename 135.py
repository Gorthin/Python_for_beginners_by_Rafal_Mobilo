colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for c in colors :
    for f in figures:
        allCards.append("%s - %s" % (c, f))

print(allCards)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []
print('=================')
max = len(allCards)

for m in range(max):
    if m %2 == 0:
        player1.append(allCards[m])
    else:
        player2.append(allCards[m])

print('p1',player1)
print('p2',player2)

print('==========')
print('==========')

player1 = allCards[:12]
player2 = allCards[12:]

print('p1',player1)
print('p2',player2)