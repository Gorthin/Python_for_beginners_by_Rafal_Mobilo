import random

for i in range(10):
    print(random.randint(1,100))

print("===============")

number1 = random.randint(1,100)
print("First number generated is %d" %(number1))

counter = 1
number2 = random.randint(1,100)

while number2 != number1:
    counter+=1
    number2=random.randint(1,100)
    print(counter,number2)

print("I needed %d attpempts to generate %d again" % (counter, number1))
