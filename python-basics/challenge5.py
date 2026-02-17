# Name : Abigail Wangechi
# Date : 16/02/2026
# Program to calculate income tax

salary = int(input("Enter your gross tax:"))

if salary < 50000:
    tax = (2.5 * salary)/100
else:
    tax = 0
net_salary = salary - tax

print(f"Gross salary = {salary}")
print(f"Net_salary = {net_salary}")
print(f"Tax = {tax}")

if salary > 50000:
    tax = (4.5 * salary)/100
else:
    tax = 0
net_salary = (salary - tax)

print(f"Gross salary = {salary}")
print(f"Net_salary = {net_salary}")
print(f"Tax = {tax}")

if  salary > 100000:
    tax = (7.5 * salary)/100
else:
    tax = 0
net_salary = (salary - tax)

print(f"Gross salary = {salary}")
print(f"Net_salary = {net_salary}")
print(f"Tax = {tax}")