# Name : Abigail Wangechi
# Date : 24/2/2026
# Program to perform file operations

#create  new file
new_file = open("student_data.txt","r+")
#write to new file
new_file.write("{Student Name : Abigail Wangechi, ID : 290765478 , Email : keshi@gmail.com}")
new_file.close()
#Read from the new file
new_file = open("student_data.txt","r+")
data = new_file.read()
print(data)
new_file.close()

# delete a file
# us os module
import os
os.remove("remove.txt")

# delete folder
os.rmdir("folder")