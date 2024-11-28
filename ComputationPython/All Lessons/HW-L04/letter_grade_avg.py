# letter_grade_avg.py
from grade_compute import find_lowest_grade, process_grades


def main():
    # Keeps running the program until the user decides to quit
    while True:
        done = process_line()
        if done:
            break  # Exits the loop if the user enters 'Q'


# Processes four line of input and appends them to the grades list
# @return True if the user has inputted Q for (quit) to end the program, False otherwise


def process_line():
    # Reads the grades with the required prompts
    print('Enter letter grades such as a, A, B+, c-, D+')
    grades = []

    # Accepts 4 grades or 'Q' to quit
    grade = input("Enter the first grade or Q to quit: ")
    if grade.lower() == 'q':
        return True  # Return True to indicate quitting
    grades.append(grade)

    grade = input("Enter the second grade: ")
    grades.append(grade)

    grade = input("Enter the third grade: ")
    grades.append(grade)

    grade = input("Enter the fourth grade: ")
    grades.append(grade)

    # Shows the entered grades
    print(f"You entered the grades: {', '.join(grades).upper()}")

    # Finds the lowest grade
    lowest_grade = find_lowest_grade(grades)
    print(f"The lowest grade of {lowest_grade.upper()} will be dropped.")

    # Calculates and display the average
    average_grade = process_grades(grades)
    print(f"The average of the remaining grades is {average_grade.upper()}")
    return False  # Continues the program


main()  # Starts the program
