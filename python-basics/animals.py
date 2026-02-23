# Name : Abigail Wangechi
# Date : 23/2/2026
# program to show inheritance in python

class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food
    
    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight} kgs")

    def eat(self,food):
        print("The animals eats {food}")

class Dog(Animal):
    def __init__(self,breed,height,food):
        super().__innit__(species,weight,food)
        self.breed = breed
        self.height = height
        self.colour = colour
    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight} kgs")

    def barks (self,food):
        print("The dog says woof woof ")

class Horse(Animal):
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food
    
    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight} kgs")

    def eat(self,food):
        print("The animals eats {food}")

