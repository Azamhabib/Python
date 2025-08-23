'''
Question 1
You work at a college admissions office. When inspecting a dataset of college applicants, you notice that some students have represented their grades with letters ("A", "B", "C", "D", "F"), whereas others have represented their grades with a number between 0 and 100.

You realize that for consistency, all of the grades should be formatted in the same way, and you decide to format them all as letters. For the conversion, you decide to assign:

"A" - any grade 90-100, inclusive
"B" - any grade 80-89, inclusive
"C" - any grade 70-79, inclusive
"D" - any grade 60-69, inclusive
"F" - any grade <60
Write a function get_grade() that takes as input:

score - an integer 0-100 corresponding to a numerical grade
It should return a Python string with the letter grade that it corresponds to. For instance,

A score of 85 corresponds to a B grade. In other words, get_grade(85) should return "B".
A score of 49 corresponds to an F grade. In other words, get_grade(49) should return "F".
Make sure that when supplying the grade that is returned by the function, it is enclosed in quotes. (For instance, if you want to return "A", you should write return "A" and not return A.)
'''

def get_grade(score):
    if score >=90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

# Get the user's input
try:
    # Convert the input to a number (float for decimal scores)
    score = float(input("Enter your score: "))
    # Call the get_grade function with the numeric score
    result = get_grade(score)
    # Print the result
    print(f"Your grade is: {result}")
except ValueError:
    # Handle cases where the input is not a valid number
    print("Invalid input! Please enter a numeric value for the score.")

'''----------------------------------------
 Case 2 pro Level 🦾 Expended Program
----------------------------------------'''

def obtain_grade(score):
    #Determines the grade based on the score.
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade ="F"
    return grade

# Feedback message

def feedback_message(grade):
    # Provide a feedback message based on the grade.
    if grade == "A":
        return "Excellent work! keep it up! 🎉"
    elif grade == "B":
        return "Great job! Alittle more effort for an A! 💪"
    elif grade =="C":
        return "Good effort! Consider reviewing some concepts to improve. 📚"
    elif grade == "D":
        return "Yor are almost there! Let's aim higher next time. 🙌"
    else:
        return "Don't give up! Failure is part of learning. You can do it !"

def main():
    # main program loop that accept score, validates them, and provides grades and feedback.

    print("Welcome to the Grade Calculator! 🎓")

    print("Enter a score between 0 and 100, or type 'quit' any time to exit")

    while True:
        # Get user input
        user_input = input("\nEnter your score: ")
        # check if the user wants to quit
        if user_input.lower() == "quit":
            print("Goodbye! keep learning and improving. 👋")
            break
        try:
            # convert input to a float for numaric comparison
            score = float (user_input)

            if score < 0 or score > 100:
                print(" Invalid score! Please enter a number 0 and 100.")
                continue

            # get the grade and feedback
            grade = obtain_grade(score)
            feedback = feedback_message(grade)

            # Display results
            print(f"\nYour grade is : {grade}")
            print(feedback)

        except ValueError:
            #Handle non-numaric input
            print("Invalid input! Please enter a numaric value for the score. ")

# Run the program
if __name__ == "__main__":
    main()



'''---------------------------------------
Question 2
In the exercise for the previous lesson, you wrote a function cost_of_project() that estimated the price of rings for an online shop that sells rings with custom engravings. This function did not use conditional statements. In this exercise, you will rewrite the function to use conditional statements. Recall that the online shop has the following price structure:

Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
Spaces and punctuation are counted as engraved units.
Your function cost_of_project() takes two arguments:

engraving - a Python string with the text of the engraving
solid_gold - a Boolean that indicates whether the ring is solid gold
It should return the cost of the project.

The function has been partially completed for you, and you need to fill in the blanks to complete the function.
---------------------------------------'''


'''----------------------------------------
Question 3
You are a programmer at a water agency. Recently, you have been tasked to write a function get_water_bill() that takes as input:

num_gallons = the number of gallons of water that a customer used that month. (This will always be an integer with no decimal part.)
It should output the water bill.

The water agency uses this pricing structure:

Tier	Amount in gallons	Price per 1000 gallons
Tier 1	0 - 8,000	$5
Tier 2	8,001 - 22,000	$6
Tier 3	22,001 - 30,000	$7
Tier 4	30,001+	$10
For example:

Someone who uses 10,000 gallons of water in a month is placed in Tier 2, and needs to pay a water bill of $6 * 10 = $60. In other words, get_water_bill(10000) should return 60.0.
Someone who uses 25,000 gallons of water in a month is placed in Tier 3, and needs to pay a water bill of $7 * 25 = $175. In other words, get_water_bill(25000) should return 175.0.
Do not round your answer. So, your answer might return fractions of a penny.
-----------------------------------------------------------------------------'''



'''--------------------------------------------------------------------------
Question 4
You work for a company that provides data services. For $100/month, your company provides 15 gigabytes (GB) of data. Then, any additional data is billed at $0.10/MB (or $100/GB, since 1,000 MB are in 1 GB).

Use the next code cell to write a function get_phone_bill() that takes as input:

gb = number of GB that the customer used in a month
It should return the customer's total phone bill.

For instance:

A customer who uses 10 GB of data in one month is billed only $100, since the usage stayed under 15 GB. In other words, get_phone_bill(10) should return 100.
A customer who uses 15.1 GB (or 15 GB + 100 MB) of data in one month has gone over by .1 GB, so they must pay $100 (cost of plan), plus $0.10 * 100 = $10, for a total bill of $110. In other words, get_phone_bill(15.1) should return 110.
Do not round your answer.
--------------------------------------------------------------------------------'''

