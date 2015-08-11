#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################

text = open('words.txt')

def words(text):
    for word in text:
        if len(word) > 20:
            print word.rstrip('\r\n')
        else:
            continue

##############################################################################
def main():
    words(text)

if __name__ == '__main__':
    main()
