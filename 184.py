import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many person are the team?')
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except ValueError as e:
    print('Sorry tou need to enter a integer number',e)

except ZeroDivisionError as e:
    print('Do not enter value 0',e)

except:
    print("Somethin went wrong",sys.exc_info()[0])
    
else:
    print("Every person shoud have around",tasksPerPerson, "tasks")

finally:
    print('Script finished with/without errors')
    
