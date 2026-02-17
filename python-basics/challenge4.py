# Name : Abigail Wangechi 
# Date : 15/2/2026
# Program for loops

import math
# print table header 
print("Angle | sin | cos | tan")
print("-------------------------")
factor = 2
for angle in range (-180,+180,30):
    x = angle * factor 
    # using round so as to reduce the decimals 
    sine = round(math.sin(x), 2)
    cosine = round(math.cos(x), 2)
    tangent = round(math.tan(x), 2) if cosine !=0 else "undefined"

    print(f"{angle:5} | {sine:5} | {cosine:5} | {tangent:5}")










