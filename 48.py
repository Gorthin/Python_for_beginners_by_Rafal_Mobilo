IsWeekend = True
print("Is weekend = ", IsWeekend)

Temp = 25
print("Temp is = ", Temp)

ToDoList = ""
print("ToDoList =", ToDoList)

IsHappy = IsWeekend and Temp >= 20 and ToDoList == ""
print("IsHappy=",IsHappy)

IsHappy = not IsWeekend and Temp < 20 and ToDoList != ""
print("IsHappy=",IsHappy)

IsHappy = IsWeekend and Temp >= 20 and ToDoList == "" \
or not IsWeekend and not Temp >= 20 and ToDoList not == ""
print("IsHappy=",IsHappy)
