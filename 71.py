# metoda gorsza

age = 22
isDrunk = True
isRestrictedArea = False

if  age < 18:
    print("You are too young and you cannot buy alcohol")
else:
    if isDrunk:
        print("Are you drunk? We cannot sell you alcohol")
    else:
        if isRestrictedArea:
            print("Restricted Area. Alcohol is forbidden")
        else:
            print("Ok, you can buy alcohol")

print("-----------------------")

if age < 18:
    print("You are too young and you cannot buy alcohol")
elif isDrunk:
    print("Are you drunk? We cannot sell you alcohol")
elif isRestrictedArea:
    print("Restricted Area. Alcohol is forbidden")
else:
     print("Ok, you can buy alcohol")

print("-----------------------")
