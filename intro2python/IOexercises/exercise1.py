#!/usr/bin/env python3

def read(title):
    with open(title, "r") as file_handle:
        contents = file_handle.read()
    print(contents)

if __name__ == "__main__":
    file = input("Please input the name of the file you wish to open: ")
    read("{}.txt".format(file))

    
