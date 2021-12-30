#! python3

musclePain = True
fever = False
weakness = True

if musclePain and fever and weakness:
    print('Suspicion of influenza')
else:
    print('The flu is unlikely')

if musclePain and fever and weakness:
    print('Suspicion of influenza')
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("you may be cold")
isMan = True
if musclePain and fever and weakness or  isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("this only cold")

isCheckCompleted = False

print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")