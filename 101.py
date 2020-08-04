persons = ['Elizabeth', 'Steven@sales.mycompany.com','sebastian', 'Margaret', 'Svetlana@mycompany.eu','Raphel']

domain = 'mycompany.com'

emails = []

for person in persons:

    if '@' in person:
        emails.append(person)
        continue
    email = person + '@' +domain
    emails.append(email)

'''
for person in persons:

    if '@' in person:
        emails.append(person)
    else:
        email = person + '@' +domain
        emails.append(email)
'''
for email in emails:
    print(email)
