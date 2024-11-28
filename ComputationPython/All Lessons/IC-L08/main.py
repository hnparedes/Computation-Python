# Some notes about self
# class Dog:

# tricks = []  mistaken use of a class variable

# def __init__(self, name):
#     self.name = name

# def add_trick(self, trick):
#     self.tricks.append(trick)


# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print('d dog is ', d.name)  correct
# print('e dog is ', e.name)  correct
# d.tricks  unexpectedly shared by all dogs

# Inheritance from base class Person

# Base class
# demonstrate inheritance
# class Person:

# Initialize
# def __init__(self, name. id):
# self.name = name
# self.id = id

# check if this person is an employee
# def display(self):
# print('employee: ', self.name, self.id)

# Derived class
# class Emp(Person):

# def print(self):
# print("The child class /Emp/ is called")

# emp_details = Emp("Tyler", 1103)

# calling parent class function
# emp_details.display()

# Calling child class function
# emp_details.print()
