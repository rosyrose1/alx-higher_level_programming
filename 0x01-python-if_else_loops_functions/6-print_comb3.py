#!/usr/bin/python3
h = 0
while h < 8:
    y = h
    while y <= 9:
        if h != y:
            print('{}{}'.format(h, y), end=', ')
        y += 1
    h += 1
print('{}{}'.format(h, y - 1), sep='')
