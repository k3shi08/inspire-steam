# Name : Abigail Wangechi
# Date : 18/2/2026
# Program to show lists in python

friends = ["Rachel","Pheobe","Ross","Chandler","Monica","Joey"]
print(friends)
friends.sort()
print(friends)

friends.reverse() #does the opposite of sort if it started with wendy now it will end with wendy
print(friends)

friends.append("Jack") #adds an item to the end of the list
print(friends)

new_friends = ["Tracy","James","Faith","Dawn","Wendy","Augustine"]
print(len(new_friends)) #gives the length of the items on the list

#new list of friends
students = friends + new_friends
print(students)

students.pop() #remove the last item of the list
print(students)

students.insert(5,"Jenny")
print(students)
students.insert(9,"Valarie")
print(students)

students.extend("James")
print(students)
students.remove("Wendy")
print(students)

new_students = students.copy()
print(new_students)