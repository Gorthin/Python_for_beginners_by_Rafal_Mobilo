number = 1
previousNumber = 0

while number <= 50:
    print("Add", number, "and", previousNumber, "is",number + previousNumber)
    previousNumber = number
    number+=1

print('---------------')

import random
my_number = random.randint(0,20)
guess = -1
print("Guess my number")
while guess != my_number:
    guess = int(input())
    if guess == my_number:
        print("Congratulation. This is my number!")
    elif guess > my_number:
        print("Sorry - my number is smaller than your guess. Try again")
    else:
        print("Sorry - my number is greater3 than your guess. Try again")

print('---------------')

import random
my_number = random.randint(0,20)
trials = 0
guess = -1
print("Guess my number")
while guess != my_number:
    guess = int(input())
    trials+=1
    if guess == my_number:
        print("Congratulation. This is my number!")
    elif guess > my_number:
        print("Sorry - my number is smaller than your guess. Try again")
    else:
        print("Sorry - my number is greater than your guess. Try again")
    print(trials)