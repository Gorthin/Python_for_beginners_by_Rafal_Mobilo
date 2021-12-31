for x in range(1,11):
    line = str(x)
    for y in range(1,11):
        line += '\t%3d' % (x*y)
    print(line)

print('===============')

i = 10
end = 1

for j in range(1, i + 1):
    end *= j

print(i, end)

print('==========')

x = 10
for i in range(1, x+1):
    end = 1

    for j in range(1, i+1):
        end *= j

    print(i, end)

print('===========')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for i in list_noun:
    for j in list_adj:
        print(i, "+", j)