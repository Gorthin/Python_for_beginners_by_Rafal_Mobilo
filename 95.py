for x in range(1,10):
    line = str(x)
    for y in range(1,10):
        line += ('\t%3d' % (x*y))
    print(line)
