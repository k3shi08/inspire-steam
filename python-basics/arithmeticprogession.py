# Name : Abigail Wangechi
# Date : 13/02/2026
# Program to calculate arithmetic progression

#Calculate nth term

a = int(input("Enter the first number:"))
n = int(input("Enter the number of terms:"))
d = int(input("Enter the common difference:"))

nth_term = a+(n-1)*d
print(f"the nth term is:{nth_term}")
sum_of_numbers = (n/2)*(2*a+(n-1)*d)
print(f"the sum of the numbers is:{sum_of_numbers}")