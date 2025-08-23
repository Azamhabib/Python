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


#----------------------------------------
# Case 2 pro Level 🦾
#----------------------------------------

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
sdfsdf