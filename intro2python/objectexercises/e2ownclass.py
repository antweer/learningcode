#1/usr/bin/env python3

#Creating my own class - It's a vehicle

class Person():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.people_greeted = []
    def __str__(self):
        return "Name: {} Email: {} Phone number: {}".format(self.name, self.email, self.phone)
    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person.name not in self.people_greeted:
            self.people_greeted.append(other_person.name)
    def print_contact_info(self):
        print("{}'s email: {}, {}\'s phone number: {}".format(self.name, self.email, 
        self.name, self.phone))
    def add_friend(self, friend):
        self.friends.append(friend)
    def num_friends(self):
        return len(self.friends)
    def num_unique_people_greeted(self):
        return len(self.people_greeted)

class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print("{} {} {}".format(self.year, self.make, self.model))

if __name__ == "__main__":
    car = Vehicle("Hyundai", "Elantra Touring", 2012)
    print(car.make, car.model, car.year)
    car.print_info()
    tanweer = Person("Tanweer", "trajwani@gmail.com", "713-499-0029")
    jj = Person("JJ", "idk", "idk")
    bridget = Person("Bridget", "idk", "idk")
    paul = Person("Paul", "idk", "idk")
    tanweer.print_contact_info()
    tanweer.add_friend("Bridget")
    print(tanweer.num_friends())
    print(tanweer)
    tanweer.greet(jj)
    tanweer.greet(paul)
    tanweer.greet(jj)
    tanweer.greet(bridget)
    tanweer.greet(paul)
    tanweer.greet(jj)
    print(tanweer.num_unique_people_greeted())
