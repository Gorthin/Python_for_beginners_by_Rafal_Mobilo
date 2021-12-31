initialCapital = 20000
percent = 0.03
maxTimesYears = 10
year = 0
capital = initialCapital
while year <= maxTimesYears:
    year+=1
    capital=round((1 + percent)*capital,2)
    print('after this years:', year, 'you will have:', capital)
else:
    print('the total capital is:', round(capital-initialCapital, 2))

print("==============")

number = 20730906
variable = number
sumDigit = 0

while variable >= 10:
    digit = variable % 10
    sumDigit += digit
    variable = variable // 10
else:
    print("sum of digits of", number, "is:", sumDigit)

print("=====")

text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''

listOfWords = text.split(' ')
wordLenght = 6
print(listOfWords)
shortWords = 0
longWords = 0
i = 0
while i < len(listOfWords):
    if len(listOfWords[i]) > wordLenght:
        longWords += 1
    else:
        shortWords += 1

    i+=1
print("Long words:" ,longWords)
print("Short words:", shortWords)