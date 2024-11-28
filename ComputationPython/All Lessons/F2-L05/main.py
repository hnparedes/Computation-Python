# Functions Without Return
# Return multiple
# values from a method using tuple
# This function returns a tuple
# def fun_test():
#     str = 'polytechnic'
#     x = 9
#     j = 54
#     k = 'stem'
#     return str, x # Return tuple
# Driver code to test above method
# str, y = fun_test() # Assign returned tuple
# z = fun_test()
# print(str)
# print(z)
# print(fun_test())

# Function With Return
# Return multiple
# values from a method using tuple
# This function returns a tuple
# def fun_test():
#     str = 'polytechnic'
#     x = 9
#     j = 54
#     k = 'stem'
#     return str, x Return tuple
# Driver code to test above method
# str, y = fun_test() # Assign returned tuple
# z = fun_test()
# print(str)
# print(z)
# print(y)
# print(fun_test())

# Lambdas[Functions]
# another_lambda
# double = lambda x: x * 2
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(double, numbers))
# print(doubled_numbers) Output: [2, 4, 6, 8, 10]

# List of builtin Functions
# dir(__builtins__)

# Docstring used to document code
# def add_binary(a, b):
"""
    Returns the sum of two decimal numbers in binary digits

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
"""
#     binary_sum = bin(a+b) [2:] start at index 2
#     return binary_sum
# print('This is the docstring --- \n',add_binary.__doc__)
# print('This is the actual function',add_binary(3,4))

# Docstrings automated in Pycharm
# def somefunction(stu_input, stu_output)
# float
"""
   Returns the oriduct of stu_input and
stu_output
   :param stu_input: qty of student hours
worked
   :type stu_input: int
   :param stu_output: qty of student pay in
dollar
   :type stu_output: int
   :return: float stu_input * stu_output
   :rtype: float
"""
#    return stu_input * stu_output
# print(somefunction(2,4))

# Importing Objects
# imports.py
# from datetime import datetime, timezone two imports on the same line
# from unittest.mock import patch single import
# import pytest third party library
# from core.models import ( # multiline import
#    Exam,
#    Exercise,
#    Solution,
# )
