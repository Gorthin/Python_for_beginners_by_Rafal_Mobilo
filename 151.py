#!/usr/bin/python3

def PrintAnimal(animal):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''

    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)

    return

PrintAnimal('cat')
PrintAnimal(animal='bear')
PrintAnimal(animal='bat')
PrintAnimal('unicorn')

#2

def DaysToEndOfYear(year, month, day):
    from datetime import date

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)

DaysToEndOfYear(2017, 2, 24)
DaysToEndOfYear(year=2019, month=3, day=22)
DaysToEndOfYear(month=5, day=12, year=2020)