import random
print("One random numer:",random.randint(1,100)) #1 <= N <= 100
print("\n")

print("One random numer from range:",random.choice(range(1,100)))
print("\n")

print("One random numer from range - easier:",random.randrange(1,100))
print("\n")      

list = ['John', 'Ann', 'Susan', 'Emily', 'Greg', 'Chris']
random.shuffle(list)
print("Reordered list:",list)
print(list[1])
print("\n")

print("Just a random float",random.random())
print("\n")
