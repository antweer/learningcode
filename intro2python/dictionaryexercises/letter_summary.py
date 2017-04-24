#!/usr/bin/env python3

def letter_histogram(word):
    letters = {}
    for x in word:
        letters.setdefault(x, 0)
        letters[x] = letters[x] +  1
    print(letters)

if __name__ == "__main__":
    letter_histogram("banana")

 
