#Create a program that asks the user for eight names of people and store them in a list.
#When all the names have been given, Pick a random one and print it.

import random

people = []

while len(people) < 8:
    name = input("Give a name of a person: ")
    people.append(name)

print ("List of people: ", people)
r = random.randint(0, len(people)-1)

print("Random person: ", people[r])