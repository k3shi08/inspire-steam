# Name : Abigail Wangechi
# Date : 17/2/2026
# Program to display a diamond and a triangle using *

rows = 5

# the top
for x in range (1, rows + 1):
    print(" " *(rows - x) + "*" *(2*x - 1))

# the bottom
for x in range(rows - 1, 0, -1):
    print(" " *(rows - x)+"*"*(2*x - 1))

