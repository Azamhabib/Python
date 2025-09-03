# Looping Through Outer Dictionary
students = {
    "Ali": {"math": 90, "science": 85},
    "Sara": {"math": 78, "science": 92},
    "John": {"math": 88, "science": 76}
}

for name, subjects in students.items():
    print("student:",name)
    print("Subject:",subjects)

# Looping inside the nested Dictionary

students = {
    "Ali": {"Math": 90, "Science": 85},
    "Sara": {"Math": 78, "Science": 92},
    "John": {"Math": 88, "Science": 76}
}

for name, subjects in students.items():
    print("Student:", name)
    for subject, score in subjects.items():
        print(" ",subject,":",score)

# Practice with Outer and Inner dictionary
students = {
    "Ali": {"Math": 90, "Science": 85},
    "Sara": {"Math": 78, "Science": 92},
    "John": {"Math": 88, "Science": 76}
}

for name,subjects in students.items():
    student = name
    for subject, score in subjects.items():
        print (student,"scored",score,"in",subject)

# simplified, without the extra student = name line
students = {
    "Ali": {"Math": 90, "Science": 85},
    "Sara": {"Math": 78, "Science": 92},
    "John": {"Math": 88, "Science": 76}
}

for name,subjects in students.items():
    for subject, score in subjects.items():
        print (name,"scored",score,"in",subject)

# Use f-string(more modern and clean code)

students = {
    "Ali": {"Math": 90, "Science": 85},
    "Sara": {"Math": 78, "Science": 92},
    "John": {"Math": 88, "Science": 76}
}

for name,subjects in students.items():
    student = name
    for subject, score in subjects.items():
        print (f"{name} scored {score} in {subject}.")

# Alignment if need(nice Tabular look)

students = {
    "Ali": {"Math": 90, "Science": 85},
    "Sara": {"Math": 78, "Science": 92},
    "John": {"Math": 88, "Science": 76}
}

for name,subjects in students.items():
    for subject, score in subjects.items():
        print (f"{name:<5} | {subject:<7} | {score}")
'''
:<5 → left-align the text inside a field that is 5 characters wide.

So:

"Ali" becomes "Ali " (with 2 spaces added to make total width = 5).

"Sara" stays "Sara " (1 space added).
'''
#add headers and print your student scores in a clean table format.
students = {
    "Ali": {"Math": 90, "Science": 85},
    "Sara": {"Math": 78, "Science": 92},
    "John": {"Math": 88, "Science": 76}
}

# Print table header
print(f"{'Name':<6} | {'Subject':<8} | {'Score':<5}")
print("-" * 30)  # separator line

# Print student scores
for name, subjects in students.items():
    for subject, score in subjects.items():
        print(f"{name:<6} | {subject:<8} | {score:<5}")


# print out put with different code

students = {
    "Ali": {"Math": 90, "Science": 85},
    "Sara": {"Math": 78, "Science": 92},
    "John": {"Math": 88, "Science": 76}
}

# ANSI escape codes for colors
GREEN = "\033[92m"
RESET = "\033[0m"

# Print table header in green
print(GREEN + f"{'Name':<6} | {'Subject':<8} | {'Score':<5}" + RESET)
print("-" * 30)

# Print student scores (normal)
for name, subjects in students.items():
    for subject, score in subjects.items():
        print(f"{name:<6} | {subject:<8} | {score:<5}")

''''
Common colors:

\033[91m → Red

\033[92m → Green

\033[93m → Yellow

\033[94m → Blue

\033[0m → Reset to default
'''