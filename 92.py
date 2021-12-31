data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for i in data:
    print(i.upper())

print('============')

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for i in data:
    elements = i.split(":")
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])

print('============')

