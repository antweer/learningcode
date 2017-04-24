#!/usr/bin/env python3


def ephonebook():
    print("Electronic Phone Book\n=====================\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit\n")
    entry = int(input("What do you want to do (1-5)? "))
    options[entry]()

def lookup():
    name = input("Name: ")
    number = phonebook[name]
    if name in phonebook:
        print("Found entry for {}: {}\n".format(name, number))
        ephonebook()
    else:
        print("Name not found.")
        ephonebook()

def setentry():
    name = input("Name: ")
    number = input("Phone number: ") 
    phonebook[name] = number
    print("Entry stored for {}.\n".format(name))
    ephonebook()

def delentry():
    name = input("Name: ")
    if name in phonebook:
        del phonebook[name]
        print("Deleted entry for {}\n".format(name))
        ephonebook()
    else:
        print("Name not found.")
        ephonebook()

def listall():
    for x in phonebook:
        print("Found entry for {}: {}".format(x, phonebook[x]))
    print("\n")
    ephonebook()

def quitbook(): 
    print("Bye!")
    quit()

phonebook = {}

options = {
    1: lookup,
    2: setentry,
    3: delentry,
    4: listall,
    5: quitbook
}

if __name__ == "__main__":
    ephonebook()

    
