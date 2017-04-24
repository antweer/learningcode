#!/usr/bin/env python3

import string

def word_histogram(text):
    tally = {}
    words = text.split()
    for x in words:
        tally[x] = text.count(x)
    print(tally)
    return tally
    
if __name__ == "__main__":
    paragraph = input("Statement: ").lower()
    word_histogram(paragraph)

    

