data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for error in data:
    print(error.upper())

print('===========')

for error in data:
    message = error.split(':')
    print(message[0].upper())
    print(message[1])

print('============')

for error in data:
    message = error.split(':')
    if message[0] == 'Error':
        print(message[1].upper())
    else:
        print(message[1])
