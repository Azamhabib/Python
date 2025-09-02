# Sets
# sets are unordered, no duplicates

fruits = {"apple", "banana","orange","apple"}
print(fruits)

'''
sets are fun because they’re all about unique items and mathematical set operations (like union, intersection).
'''
# Creating a set
nums={1,2,3,4,4,5}
print(nums) #Duplicates removed

#Common operation on sets
# Add/Remove elements

fruits ={"apple","banana"}
fruits.add("orange") # add one item
print(fruits)
fruits.remove("banana") #remove item(error if not found)
print(fruits)
fruits.discard("grapes") # safe remove (no error if value is missing)
print(fruits)

#set operations
a={1,2,3,4,5}
b={3,4,5,6,7}

print(a.union(b))

print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

# Membership
a={1,2,3,4,5}
b={3,4,5,6,7}
print(2 in a)
print(7 in b)

# Mathematical Shortcuts
a={1,2,3,4,5}
b={3,4,5,6,7}

print(a | b) # union
print(a & b) # Intersection
print(a - b) # difference
print(a ^ b) # symmetric difference(items in one ser or the other,not both)

# Exercise: Working with Sets
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a | b) # union
print(a & b) # Intersection
print(a - b) # difference
print(3 in b) # symmetric difference(items in one ser or the other,not both)

'''
✨ Sets are especially useful when you need unique values 
only or want to compare groups of data.
'''

#Disctionaries
#Store data in key value pairs
# creating dictionaries

student ={ 
    "name": "Azam",
    "age": 25,
    "grade": "A"
}
''' 
Here:
"name", "age", "grade" are keys
"Azam", 25, "A" are values'''

student = {"name": "Ali","age": 21,"grade": "A"}
print(student["name"])
print(student)

# Accessing Values
print(student["name"])# Output: Ali
print(student["age"])    # Output: 21

# adding/Updating
student = {"name": "Ali","age": 21,"grade": "A"}
student["age"] = 26 # update
student["subject"] = "Math" # Add new key-value pair

print(student)

# Removing
student.pop("grade")

print(student)

# check if a key exists
student= {"name": "Ali", "Age": 32, "grade": "A"}
if "name" in student:
    print("yes, name exist.")

# Looping through dictionary

student = {"name": "Ali","age": 21,"grade": "A"}
for key,value in student.items():
    print(key, ":", value)

# Get only keys or only values
student = {"name": "Ali","age": 21,"grade": "A"}
print(student.keys())    # dict_keys(['name', 'age', 'city'])
print(student.values())  # dict_values(['Azam', 25, 'Karachi'])

# Length of dictionary
student = {"name": "Ali","age": 21,"grade": "A"}
print(len(student)) # Number of key value pairs

fruit = {"apple": 5, "banana": 3, "mango": 7}
fruit["banana"] += 2
print(fruit)
#
cart = {"apple": 5, "banana": 3, "mango": 7}
cart ["apple"] += 2 #update apple value
cart ["mango"] =4 # adding new item
cart.pop("orange",None)
print(cart)
'''
⚖️ Between these two, sets are lighter and simpler. Dictionaries are super important for Data Science
(because you’ll later see JSON, Pandas DataFrames, etc.).
'''

#Loop over keys 
#Example idea (not code, just structure):
'''
for key in cart:       # loop over keys
for value in cart.values():  # loop over values
for key, value in cart.items():  # loop over both

'''
cart ={"apple":4, "ornage": 5, "mango": 3}
for key in cart.keys(): #cart.keys() gives only the keys
    print(key)


#Loop over values
cart = {"apple": 4, "banana": 5, "mango": 2}

for value in cart.values(): #cart.keys() give only the values
    print(value)

#Loop over both key and value
cart ={"apple":4, "ornage": 5, "mango": 3}
for key,value in cart.items(): # cart.items() give both key and value togather
    print(key,":",value)

'''
.items() isn’t about ending the loop it’s about telling Python:
Give me the dictionary as key value pairs so I can use both in my loop.'''

cart = {"apple": 4, "banana": 5, "mango": 2}
for x in cart:
    print(x) # return key values
#Python’s default behavior is to loop over the keys only.

# print the both values without .items()

cart = {"apple": 4, "banana": 5, "mango": 2}
for key in cart:
    # use the key to find ite value in the loop
    value = cart[key]
    print (key, value)

'''
The next natural step is to practice nesting (a dictionary inside another dictionary, or list inside a dictionary). This is super important in Data Science, because real datasets often look like that.
For example, think about a dictionary of students and their exam scores:
students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}
With this kind of structure, you can:

Access one subject score → students["Ali"]["math"]

Loop through all students and subjects

Do calculations (like averages)

-----Identification the Keys in the nesty dictionary----

Here we actually have two levels of keys:

    1-Outer dictionary keys → "Ali", "Sara", "John"

        These are the student names.

        Each one points to another dictionary.

    2-Inner dictionary keys → "math", "science"

        These are the subjects.

        Each one points to a number (the score).

So:

"Ali" is a key in the outer dictionary.

"math" is a key inside Ali’s dictionary.
'''
students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}
print(students.keys()) # dict_keys(['Ali', 'Sara', 'John'])

print(students["Ali"].keys()) # dict_keys(['math', 'science'])

# wanted to get Ali’s science score
students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}
print(students["Ali"]["science"])

#Print sara's subject names(not the score, just the subject)

students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}
print(students["Sara"].keys())

#loop through all of Sara’s subjects:
students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}
for subject in students["Sara"].keys(): # subject can be any value e.g x or i
    print(subject)

#practice looping over all students to print their subjects and marks? That would combine dictionary + loop nicely.
students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}

for name,subject in students.items():
    print("student:", name, "Science score:",subject["science"])

# how to calculate the average xcience score for all students using a loop

students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}

total = 0 
count = 0
for name,subjects in students.items():
    total += subjects["science"] # add each science score
    count += 1 # count eash student

average = total /count
print ("Average Science score is :",average)    

# how to find the highest science score and which student got it?

students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}

heighest_score = -1 # start with the low value 
top_student = "" # to store the name of the student

for name,subjects in students.items():
    if subjects["science"] > heighest_score:
        heighest_score = subjects["science"]
        top_student = name

print ("Top student in science is:", top_student, "with score:",heighest_score)

#-------------------------------------------------------
#Practice challenge
'''
We’ll use the same students dictionary.

👉 Your task:

Loop through the dictionary.

Find the highest math score and the student who got it.

Find the lowest math score and the student who got it.

Print both results at the end
'''
students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}
heighest_score= -1
lowest_score = 101
top_student = ""
low_student = ""
for name,subjects in students.items():
    if subjects["math"] > heighest_score:
        heighest_score = subjects["math"]
        top_student =name
        
    if subjects["math"] < lowest_score :
            lowest_score = subjects["math"]
            low_student = name
            
print(top_student,"got the heightest score in math and his score is:", heighest_score)
print(low_student,"got the lowest_score in math and his score is:",lowest_score)
