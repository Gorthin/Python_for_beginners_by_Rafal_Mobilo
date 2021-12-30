shoesize = 43
birth = 1988
number = (shoesize*5 +50)*20 + 1017 - birth
print('shoe size is:',number //100)
print('birth date is:',number %100)

x = 678
print('This should be 5: ', (x*2+10)/2-x)

presence = 0.85
note = 3.5
finalWork = False
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
presence = 0.4
note =2.5
finalWorkOK = True
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)