#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# my code is here
r = abs(number) % 10
# r for last digits
if number < 10:
    r *= -1
if r > 5 and r != 0:
    print('Last digit of {} is {} and is greater than 5'.format(number,
                                                                r))
elif r < 6 and r != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'
          .format(number, r))
else:
    print('Last digit of {} is {} and is 0'.format(number, r))
