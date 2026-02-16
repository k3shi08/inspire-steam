# Name : Abigail Wangechi
# Date : 16/02/2026
# Program to calculate income tax

salary = int(input("Enter your gross tax:"))

if salary < 50000:
    tax = (2.5 * salary)/100
    net_salary = salary - tax
print(f"Gross salary = {salary}")
print(f"net_salary = {net_salary}")
print(f"tax = {tax}")