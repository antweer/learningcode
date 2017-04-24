#!/usr/bin/env python3

def write(title):
    content = input("Please input what you want to add to the file: ")
    with open(title, "w") as file_handle:
        file_handle.write(content)

if __name__ == "__main__":
    file = input("Please input the name of the file you want to open: ")
    write("{}.txt".format(file))

    
