#!/usr/bin/python3
c = 0
while c < 100:
    if c != 99:
        print('{0:02d}'.format(c), end=', ')
    else:
        print(c)
    c += 1
