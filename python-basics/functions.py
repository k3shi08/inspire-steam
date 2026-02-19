# Name : Abigail Wangechi
# Date : 19/2/2026
# Program to cook an egg

def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 2
    print(f"The pan is {pan} , and the fire is {moto}, add {oil} amount of oil and cook {eggs} eggs")

print("Here is statement 1")

print ("Here is statement 2")

cook_egg()

print("Here is statement 3")

# Ride fare creating function

def create_fare(route,distance,is_rush_hour):

    fare = distance * 10
    if is_rush_hour == True:
        fare = fare * 1.5
    print(f"The fare on route {route} , is {fare}")

    return fare

rush_hour = True
returned_fare = create_fare("Juja-Allsops",7,rush_hour)
print(f"The fare returned is :{returned_fare}")


# Passing a list as a paramater
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")

all_interests = ["formula 1","reading novels","going for walks"]

write_all_interests(all_interests)