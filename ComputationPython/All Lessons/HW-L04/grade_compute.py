# grade_compute.py

# Converts letter grades to numbers
def grade_to_number(grade):
    grades = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'F': 0.0
    }
    return grades.get(grade.upper(), 0.0)

# Converts numbers back to letter grades to return the grade letter


def number_to_grade(number):
    if number >= 4.3:
        return "A+"
    elif number >= 4.0:
        return "A"
    elif number >= 3.7:
        return "A-"
    elif number >= 3.3:
        return "B+"
    elif number >= 3.0:
        return "B"
    elif number >= 2.7:
        return "B-"
    elif number >= 2.3:
        return "C+"
    elif number >= 2.0:
        return "C"
    elif number >= 1.7:
        return "C-"
    elif number >= 1.3:
        return "D+"
    elif number >= 1.0:
        return "D"
    else:
        return "F"


# Finds the lowest grade


def find_lowest_grade(grades):
    numeric_grades = [grade_to_number(g) for g in grades]
    min_grade = min(numeric_grades)
    min_grade_index = numeric_grades.index(min_grade)
    return grades[min_grade_index]

# Process the grades by dropping the lowest and calculating the average


def process_grades(grades):
    numeric_grades = [grade_to_number(g) for g in grades]
    lowest_grade = min(numeric_grades)
    numeric_grades.remove(lowest_grade)

    average = sum(numeric_grades) / len(numeric_grades)
    return number_to_grade(average)
