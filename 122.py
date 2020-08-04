import random

min = 1
max = 6
dice = random.randint(min, max)

if dice == 1:
    print('''   
 o 
   
 ''')
elif dice == 2:
    print('''  o
   
o  
 ''')
elif dice == 3:
    print('''  o
 o 
o  
 ''')
elif dice == 4:
    print('''o o
   
o o
 ''')
elif dice == 5:
    print('''o o
 o 
o o
 ''')
else:
    print('''o o
o o
o o''')

print('==========')

dice = []

for i in range(5):
    dice.append(random.randint(min, max))

dice.sort()
print(dice)

