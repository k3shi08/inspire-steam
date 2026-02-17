# Name : Abigail Wangechi
# Date : 17/02/2026
# Program to perform arithmetic operations

f_number = 12 # first no
s_number = 34 # second no
sum_numbers = f_number + s_number
diff_numbers = f_number - s_number
product_numbers = f_number * s_number
quotient_numbers = f_number / s_number

print("The sum of the numbers %d"%sum_numbers)
print("The quotient of the numbers %0.2f"%product_numbers)

#modulus - remainder
print(7%5)

# even and odd numbers
for x in range (0,21):
    if(x%2==1):
        print(f"{x} is an odd number")
    elif(x%2==0):
        print(f"{x} is an even number")

