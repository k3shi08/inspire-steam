# Name : Abigail Wangechi
# Date : 19/2/2026
# Program to create classes

class Human:
    # First we define the attribute of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Eldoret"

    # We then create a constructor for the class object
    # The constructor will be used to create copies of this object
    def __init__(self, name ,age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, I am {self.human_name}. Here is my story")
        print(f"There was once a bot that said hello world")

# Create the humans
amani = Human("Amani",17)
triza = Human("Triza",18)

# Let the humans created do thinga
amani.tell_story()
print("Amani's age is: amani_human_age")

# Modify one of the objects , without modifying other objects
print("Triza's location:", triza.city)
print("Amani's location:", amani.city)

triza.city = "Nairobi"






