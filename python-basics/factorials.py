# Name : Abigail Wangechi
# Date : 16/02/2026
# Program to calculate the factorials of numbers

factorial = 1  # initialize factorial 1
number = int(input("enter the number x:"))
for x in range (1,number+1):
    factorial*=x
    
print(f"{number}!={factorial}")


