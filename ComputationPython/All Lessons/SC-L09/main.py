# Notes about Super()
# oop/super.implicit.py
# class Book:
#     def __init__(self, title, publisher, pages):
#         self.title = title
#         self.publisher = publisher
#         self.pages = pages


# class Ebook(Book):
#     def __init__(self, title, publisher, pages, format_):
#         super().__init__(title, publisher, pages)
#         self.format_ = format_


# ebook = Ebook(
#   'Learn Python Programming', 'Packt Publishing', 500, 'PDF')
# print(ebook.title)
# print(ebook.publisher)
# print(ebook.pages)

# Method Resolution Order
# oop/mro.simple.py
# class A:
#     label = 'a'


# class B(A):
#     label = 'b'


# class C(A):
#     label = 'c'


# class D(B, C):
#     pass


# d = D()
# print(d.label) Is it 'b' or 'c'

# Static Methods
# some_static.py
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#     self.__priv = 10 super private value

#     @staticmethod
#     def get_max_value(x,y):
#         return max(m,y)
# Create an instance of MyClass
# obj = MyClass(10)

# print(MyClass.get_max_value(20, 30))

# print(obj.get_max_value(20, 35))
# print(obj.get_Value()) Output: 10

# Class Methods
# class my_class:

# @classmethod

# def function_name(cls, arguments):
# Function Body return value

# class my_class:

# @staticmethod

# def function_name(arguments):
# Function Body return value

# oop/class.methods.factory.py
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     @classmethod
#     def from_tuple(cls, coords): cls is Point
#         return cls(*coords)
#     @classmethod
#     def from_point(cls, point): cls is Point
#         return cls(point.x, point.y)
# p = Point.from_tuple((3, 7))
# print(p.x, p.y) 3 7
# q = Point.from_point(p)
# print(q.x, q.y) 3 7

# Use of static and class methods
# demonstrate class and static method
# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# a class method to create a Person object by birth year
# @classmethod
# def fromBirthYear(cls, name, year):
#     return cls(name, date.today().year - year)

# a static method to check if a Person is adult or not
#     @staticmethod
#     def isAdult(age):
#         return age > 18
# person1 = Person('jose', 21)
# person2 = PErson.fromBirthYear('mirriam', 1996)

# print(person1.age)
# print(person2.age)

# print the result
# print(Person.isAdult(22))

# oop/private.attrs.fixed.py
# class A:
# x = 75
# _x = 85
# __x = 95
# def __init__(self, factor):
# self.__factor = factor
# def op1(self):
# print('Op1 with factor {}...'.format(self.__factor))

# class B(A):
# def op2(self, factor):
# self.__factor = factor
# print('Op2 with factor {}...'.format(self.__factor))
# obj = B(100)
# obj.op1() Op1 with factor 100...
# obj.op2(42) Op2 with Factor 42...
# obj.op1() Op1 with factor 100...
# print('A.x', A.x)
# print('A._x', A._x)
# print('A.__x', A.__x)
# obj_a = A
# print('obj_a._x', obj_a._x)
