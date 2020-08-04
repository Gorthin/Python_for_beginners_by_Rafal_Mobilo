countries = ['FR', 'US', 'DE', 'RU']
countries[1]='GB'
print(countries[1])
countries.append('PL')
countries.insert(2, 'ES')
countries.remove('RU')
countries.sort()
countries.reverse()
print(countries.pop(2))
print(countries.index('PL'))
#print(countries.index('US'))
print(countries.count('DE'))

newList = ['FI', 'SE']
countries.extend(newList)

countriesCopy = countries.copy()
countriesCopy.clear()

print(countries)
print(countriesCopy)
