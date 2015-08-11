#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################
from __future__ import print_function

def even_odd():
    while True:
        num = raw_input('> ')
        try:
            num = int(num)
            break
        except:
            print ("That's not a number, try again!")
    if num % 2 == 0:
        print ("That's an even number")
    else:
        print ("That's an odd number")
    pass

def ten_by_ten():
    for x in range (1, 11):
        for y in range (1, 11):
            print ('{:3}'.format(x*y), end=' ') #This is a 10x10 table w/ for loops
    print()

def find_average():
    total = 0
    numbers = 0
    while True:
        num = raw_input('Enter a number, or done when finished: ')
        try:
            num_int = int(num)
        except:
            if num == 'done':
                break
            else:
                print ("Try using a number")
        if num_int > 0:
            value = float(num_int)
            total = total + value
            numbers = numbers + 1
            average = total / numbers
            print ('Average: ', average)

##############################################################################
def main():
    even_odd()
    ten_by_ten()
    find_average()
    pass

if __name__ == '__main__':
    main()
