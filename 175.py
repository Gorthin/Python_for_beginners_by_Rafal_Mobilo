#!/usr/bin/python3
'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10'''

file_path = r'd:\Python\Udemy_Python_dla_poczatkujacych\orders.csv'
with open(file_path, 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        #print(line)

        if order == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!" % line)

print("Process file ending")