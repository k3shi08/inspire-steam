# Name : Abigail Wangechi
# Date : 23/2/2026
# Program to show classes in python

class Car():
    # attributes of the car
    def __init__(self,model,make,colour,year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year

# print details
def print_details(self,model,make,colour,year):
    print(f"{make} {model} of colour{colour} manufactured in the year {year}")

# Instantiate an object

my_car = Car("Atenza","Mazda","Red","2022")
dads_cars = Car("Land cruiser","Toyota","Black","2023")

my_car.print_details("Atenza","Mazda","Red","2022")

    
