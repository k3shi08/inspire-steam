# Name : Abigail Wangechi
# Date : 17/02/2026
# Program to format the output in different styles

name = "Abigail Wangechi"
weight = 85 # weight in kgs
fav_team = "Liverpool"
height = 126.86 # height in cm

# 1. Format using print(f"{}")
print(f"my name is {name} and i weigh {weight}kgs.")

# 2. Using f string starts with f 
msg = f"My name is {name} and I support {fav_team}"
print(msg)

# 3. Using {} and .format()
print("My name {0} and I am {1} cms tall".format(name,height)) 

# 4. Using output specifiers %s - strings %f - float
import math
print('The value of pi is approximately')
print("I support %s"fav_team)
