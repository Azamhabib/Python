#if, elif, and else
'''
Basic Structure

if condition:
    code runs if condition is True
elif    
    code runs if the first was False, but this is True
else:
    code runs if none of the above are True

'''
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")

elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

marks = int(input("Enter your marks:- "))

if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")
elif marks >=50:
    print("Grade: C")

else:
    print("Grade: F")
#------------------------------------------------
# While Loop
#------------------------------------------------

count = 0
while count <= 5:
    print("Hello", count)
    count += 1
# #Pseudocode
# set count = 5
# while count > 0:
#     print(count)
#     decrease count by 1

# print("Blast off!")

count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# for Loop
for i in range(6):
    print("Hello", i)

#range(start, stop, step)

for i in range(2,11,2):
    print(i)

for i in range(10,0,-2):
    print(i)

for i in range(10,0,-3):
    print(i)