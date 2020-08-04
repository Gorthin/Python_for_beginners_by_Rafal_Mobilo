string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)

for i in range(9):
    if i %2 == 0:
        print(string_A)
    else:
        print(string_B)

x = 0
for i in range(9):
    print('x'* i)

for i in range(9):
    if i %2 == 0:
        print('o'*i)
    else:
        print('x'* i)