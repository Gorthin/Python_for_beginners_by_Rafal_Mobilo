lista =['g', 'a', 'c', 'b', 'd']
lista.sort()
print(lista)

hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN',
              'RIDERS ON THE STORM','WISH YOU WERE HERE']
print(hitsTitles)

hitsTitles.append('Child in Time')
hitsTitles.append('Again')
hitsTitles.insert(2,"HOTEL CALIFORNIA")
hitsTitles.insert(0,'THE SOUND OF SILENCE')
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove("HOTEL CALIFORNIA")
hitsTitles[0]='ENJOY THE SILENCE'
print(hitsTitles)

hitsToRead = hitsTitles.copy()
hitsToRead.sort()
print(hitsTitles)
print(hitsToRead)
hitsToRead.pop(3)
print(hitsToRead)
additionalSongs = ['NOTHING COMPARES 2 U' , 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead)
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))
hitsToRead.clear()
print(hitsToRead)