import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many person are the team?')
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except:
    print("Somethin went wrong",sys.exc_info()[0])

print("Every person shoud have around",tasksPerPerson, "tasks")
