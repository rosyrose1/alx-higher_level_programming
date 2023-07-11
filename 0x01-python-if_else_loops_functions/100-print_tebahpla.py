#!/usr/bin/python3
for n in range(ord('z'), ord('a') - 1, -1):
    if n % 2 == 0:
        m = 0
    else:
        m = 1
    print('{:s}'.format(chr(n - (m * 32))), end='')
