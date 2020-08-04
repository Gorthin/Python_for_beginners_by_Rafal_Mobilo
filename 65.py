CountryLeaders = {'PL':'Duda', 'US':'Trump'}

#print(CountryLeaders['US'])
CountryLeaders['DE'] = 'Merkel'

#print(CountryLeaders.keys())
#print(CountryLeaders.values())
#print(CountryLeaders.items())

#print(CountryLeaders.popitem())

#print(CountryLeaders.setdefault('FR', 'Macron'))

#print(CountryLeaders.get('RU'))

print(CountryLeaders)


NewLeaders = {'RU':'Putin', 'DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)




print(CountryLeaders)
                  
