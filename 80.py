firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print("Row number ", currentRow)
    currentRow += 1


#2

i = 1
imax =13

while i <= imax:
    print("Quadratic:", i, i ** 2)
    print("Cube:", i, i ** 3)
    i += 1

#3

x = 0
xmax = 16

while x <= xmax:
    print("Quadratic of two per", x, ":", 2 ** x)
    x += 1

#4

start = 1
end = 15

number = start
while number <= end:
    print(number * 'x')
    number += 1