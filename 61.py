hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HAEVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
print(hitsTitles)

hitsTitles.insert(2, 'HOTEL CALIFORNIA')
print(hitsTitles)

hitsTitles.insert(0, 'THE SOUND OF SLICE')
print(hitsTitles)

print(hitsTitles.index('HOTEL CALIFORNIA'))
print(hitsTitles.remove('HOTEL CALIFORNIA'))
hitsTitles[0] = 'ENJOY THE SILENCE'
print(hitsTitles)

hitsTitlesCopy = hitsTitles.copy()
hitsTitlesCopy.reverse()
print(hitsTitlesCopy)

hitsTitlesCopy.sort()
print(hitsTitlesCopy)

print(hitsTitlesCopy.pop(0))
print(hitsTitlesCopy.pop(0))
print(hitsTitlesCopy)

additionalSong = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hitsTitlesCopy.extend(additionalSong)
print(hitsTitlesCopy)
print(hitsTitlesCopy.count('WISH YOU WERE HERE'))
print(hitsTitlesCopy.count('RIDERS ON THE STORM'))

hitsTitlesCopy.clear()
print(hitsTitlesCopy)
