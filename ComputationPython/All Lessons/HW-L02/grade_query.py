# Initializes an empty dictionary to store student names and grades
grades = {}

# Starts an infinite loop to continuously prompt user for input
while True:
    # Asks the user for their desired action and convert input to lowercase
    user_choice = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").lower()

    # If user chooses to add a new student and grade
    if user_choice == 'a':
        # Asks for the student's name
        name = input("Enter the name of the student: ")
        # Asks for the student's grade and convert it to a float
        grade = float(input("Enter the student's grade: "))
        # Adds the student's name and grade to the dictionary
        grades[name] = grade

    # If user chooses to remove an existing student
    elif user_choice == 'r':
        # Asks for the student's name to remove from the dictionary
        name = input("What student do you want to remove: ")
        # Removes the student from the dictionary
        grades.pop(name)

    # If user chooses to modify an existing student's grade
    elif user_choice == 'm':
        # Asks for the student's name whose grade needs modification
        name = input("Enter the name of the student to modify: ")
        # Gets the student's current grade from the dictionary
        old_grade = grades[name]
        # Prompts for the new grade, showing the current one for reference
        new_grade = float(input(f"The old grade is {old_grade}.\nEnter the new grade: "))
        # Updates the student's grade with the new value
        grades[name] = new_grade

    # If user chooses to print all student grades and the average
    elif user_choice == 'p':
        # Calculates the average of all grades in the dictionary
        average = sum(grades.values()) / len(grades)
        # Print the average grade
        print(f"The average grade is {average}")
        # Iterates over all students and their grades, printing each
        for name, grade in grades.items():
            print(f"{name}: {grade}")

    # If user chooses to quit the program
    elif user_choice == 'q':
        # Prints a goodbye message and exit the loop
        print("Goodbye!")
        break

    # Handles invalid input by showing an error message
    else:
        print("Wrong input, try again")
