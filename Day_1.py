# Variables & data types (int, float, string, bool)
# Variables: I love your “cabinet” analogy. One tiny addition—you can also change what’s inside the cabinet later on (variables are reusable).
# declare Variables Like this
name= 'Azam' # String
Fullname= " Azam Habib "
x =" 123"
z = '''Multiline String''' # multiline string
Result = False # Boolen
number= 123
y = 3.4 # Float
c = 3 + 4j #Complex numbers → Python actually supports numbers with an imaginary part, like:
print(c) #(3+4j)
print(c.real) #(3.0)
print(c.imag) # (4.0)
nothing = None #NoneType → This is a special type that represents “nothing” or “no value”:

# Conversion
#Type conversion → You can convert between types. For example:
x = "123"
number = int(x)   # changes string type to integer
print (x)
y= 3.5
number = int(y) # change float to int 
print(y)
# Integers: Yes, exactly—whole numbers, positive or negative. Example: -10, 0, 45.

# Floats: Correct—they’re numbers with decimals, like 3.14 or -0.001.

# Strings: Perfect—you can use single, double, or triple quotes, and triple quotes allow multi-line text.

# Booleans: You’re spot on that they’re used for “yes/no” or “true/false” situations. In Python, we usually write them as True and False (with capital letters). They’re not exactly the same as 0 and 1, though they can act that way in math-like operations.
#_______________________________________________________________________________
#Operators

# There are a few main categories in Python:

# Arithmetic operators → +, -, *, /, %, //, **

# Comparison operators → ==, !=, <, >, <=, >=

# Logical operators → and, or, not

# Arithmetic operators

a = 10
b = 3
print(a+b) #Plus
print(a-b) #Minus
print(a*b) #Multiplacation
print(a/b) #Division
print(a//b) #floor division (whole number result, no decimal)
print(a%b) # Remainder after division
print(a**b) # exponentiation (power)

#Comparison operators → ==, !=, <, >, <=, >=
#Comparison operators always return a boolean (True or False).

x = 5
y = 7

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x >= y)   # False

#Python also lets you chain comparisons.
# # 5 < 10 < 20
print(5 < 10 < 20)

# Logical operators → and, or, not

x = True
y = False

print(x and y) # and means both must be True.
print (x or y) # or means at least one must be True.
print(not x) # not flips the value. Since x = True, not x becomes False.
print(x)

a = True
b = True
c = False

print(a and b or c)

'''a = True, b = True So True and True → True.
Since c = False, and this is True
That’s why the final answer is True.
'''
print(not c)

# input() and Concatination

name = input("Enter your name: ") #receive input from the user and save it in the variable
print("Hello,",name) # Concatenate string


