#!/usr/bin/python3
m = 0
while m < 26:
    if m != 4 and m != 16:
        print('{:c}'.format(m + 97), end='')
    m += 1
