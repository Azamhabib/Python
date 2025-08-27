for i in range(1,10):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

#exam scores in a list like [95, 72, 40, 88].How do you think we could use a loop + if/else to print “Pass” or “Fail” for each student?
exam_score = [95, 72, 40, 88]

for i in exam_score:
    if i >= 60:
        print("You passed")
    else:
        print("You failed")

'''
--------------------------------------------------Exercise 1:
Even or Odd Checker

Create a list of numbers from 1 to 10.

Use a for loop and if/else to print whether each number is "Even" or "Odd".
--------------------------------------------------'''
number = [1,2,3,4,5,6,7,8,9,10]
for i in number:
    if i % 2 == 0:
        print(i,"This is the even number")
    else:
        print(i,"This is an odd number")

'''
--------------------------------------------------
Exercise 2: Counting with While Loop

Start with count = 1.

Use a while loop to print "Number X" until it reaches 5.

Inside the loop, use if/else to print "Small" if the number is less than 3, otherwise "Big".
--------------------------------------------------
'''
count = 1
while count <= 5:
    if count < 3:
        print(f"Number {count} is smaller than 3.")
    else:
        print("Number",count,"is bigger than 3.")
    count += 1

'''
-------------
Exercise 3: Student Grades

Create a list of exam scores: [95, 72, 40, 88, 100, 53].

Use a for loop + if/elif/else to assign "A", "B", "C", or "Fail".
--------------------------------------------------'''
exam_score= [95,72,40,88,100,53]
for i in exam_score:
    if i >=90:
        print(f"Your Score is: {i}, and your grade is A.")
    elif i >=80:
        print (f"Your score is: {i}, and your grade is B.")
    elif i >=70:
        print (f"Your score is: {i}, and Your grade is C.")
    else:
        print(f"Your score is: {i}, and you are Fail.")

'''
----------------------------------
Exercise 4: Sum Until Limit (while loop)

Start with a list [5, 10, 15, 20, 25].

Use a while loop to add numbers one by one until the sum is greater than 40.

Print the final sum.
----------------------------------
'''
num = [5,10,15,20,25]
total=0
index=0
while total <= 40 and index < len(num):
    total += num[index]
    index += 1  
print("The final sum is:", total)

'''
----------------------------------
Exercise: Count Down

Write a program that:

Starts from 5

Prints numbers down to 1

Then prints "Blast off!"
-----------------------------------'''
count =5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

'''
----------------------------------
Exercise: Keep Asking Until "quit"

Write a program that:

Asks the user to enter a word (using input())

Keeps asking again and again in a while loop

Stops only when the user types "quit"

Prints "Goodbye!" at the end
------------------------------------
'''
user_input = "" # start with empty string
while user_input.strip().lower() != "quit": # loop until quit
    user_input = input("Enter a word (or type 'quit' to exit):-")

print("Goodbye!")

'''
Exercise: Sum Until 50

You have a list: [5, 12, 8, 20, 15]

Use a while loop to keep adding numbers from the list into a running total

Stop as soon as the total is greater than 50

Print the final total
'''
numbers = [5, 12, 8, 20, 15]
total = 0  
index = 0
while total <= 50 and index < len(numbers):
    total += numbers[index]
    index += 1

print("The final total is:", total)

'''
Tuples
'''
numbers = (10,20 ,30)
print(numbers[0]) # print first element of the tuple

#Indexing and Slicing
nums = (10,20,30,40)
print(nums[1]) # print the value on index 1
print(nums[1:3]) # start with index 1 inclusive end with index 3 excluded.

#Lenght
nums=(10,20,30,40,50,60,70)
print(len(nums)) # answer 7

# Membership check(in)

nums = (10,20,30,40,50)
x = 20 in nums
print(x)
print(20 in nums)
print(60 in nums)

# Concatenation and Repetition

a = (1,2,3,4,)
b = (3,4,5,6,7)
print(a+b) #(1, 2, 3, 4, 3, 4, 5, 6, 7)
print(a*3) #(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# Iterration with loop

nums = (20,12,30,40,50)
for item in nums:
    print (item)

# Count and Index method
nums=(10,20,20,30,40)
print(nums.count(20)) # 2
print(nums.index(30)) # 3

'''Special use in Data Science:
Tuples are often used for coordinates, paired data, or fixed categories 
(e.g., (latitude, longitude) or (row, column)).
'''
#Mathematical operations with tuples
#sum() works if the tuple contains numbers
nums = (10,20,30)
print(sum(nums)) # 60
# min()and max() also work
print(min(nums)) #10
print(max(nums))#30

'''
But direct arithmetic between tuples is not allowed
(1, 2, 3) + (4, 5, 6)   # Concatenates → (1, 2, 3, 4, 5, 6)
(1, 2, 3) * 2           # Repeats → (1, 2, 3, 1, 2, 3)

# ❌ (1, 2, 3) + 5   → Error
# ❌ (1, 2, 3) * (4, 5, 6) → Error
'''

#Loop if you want elemen-wise math:
nums = (1,2,3)
doubled = tuple(x*2 for x in nums) # x can be any letter e.g:i 
print(doubled)

'''
So tuples don’t behave like NumPy arrays (which allow vectorized math).
But they can hold numbers, and you can use functions like sum, 
min, max, or loops to perform math.
'''

