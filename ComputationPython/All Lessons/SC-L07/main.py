# Object Oriented Programming
# oop/simplest.class.py
# class Simplest(): when empty,braces are optional
#     pass
# print(type(Simplest)) what type is this object?
# simp = Simplest() simp is the instance object?

# Class namespaces
# oop/class.namespaces.py
# class Person:
#     species = 'Human'

# print(Person.species) Human
# Person.alive = True Added dynamically!
# print(Person.alive) True

# man = Person()
# print(man.species) Human (inherited)
# print(man.alive) True (inherited)

# Person.alive = False
# print(man.alive) False (inherited)

# man.name = 'Darth'
# man.surname = 'Vader'
# print(man.name, man.surname) Darth Vader

# Attribute shadowing
# oop/class.attribute.shadowing.py
# class Point:
#     x = 10
#     y = 7
# p = Point()
# print(p.x) 10 (from class attribute)
# print(p.y) 7 (from class attribute)
# p.x = 12 p gets its own 'x' attribute
# print(p.x) 12 (now found on the instance)
# print(Point.x) 10 (class attr the same)
# del p.x we delete instance attribute

# print(p.x) 10 (now search has to go again to find class attr)

# p.z = 3 let's make it a 3D point
# print(p.z) 3
# print(Point.z)
# AttributeError: type object 'Point' has no attribute 'z'

# The self argument
# oop/class.self.py
# class Square:
#     side = 8
#     def area(self): self is a reference to an instance
#         return self.side ** 2
# sq = Square()
# print(sq.area()) 64 (side is found on the class)
# print(Square.area(sq)) 64 (equivalent to sq.area())
# sq.side = 10
# print(sq.area()) 100 (side is found on the instance)

# The __int__ method
# oop/class.init.py
# class Rectangle:
#     def __int__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#     def area(self):
#         return self.side_a * self.side_b
# r1 = Rectangle(10, 4)
# print(r1.side_a, r1.side_b) 10 4
# print(r1.area()) 40
# r2 = Rectangle(7, 3)
# print(r2.area()) 21
