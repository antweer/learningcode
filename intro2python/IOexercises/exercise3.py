#!/usr/bin/env python3

from letter_summary import letter_histogram
from word_summary import word_histogram

def return_content(title):
    with open(title, "r") as file_handle:
        content = file_handle.read()
    return content

if __name__ == "__main__":
    filename = input("Input filename: ")
    text = return_content("{}.txt".format(filename))
    print(text)
    letter_histogram(text)
    word_histogram(text)
