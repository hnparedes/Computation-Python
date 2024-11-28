# Why functions
# tax.no_function.py
# done = False
# while not done:
#     sentinel = str.upper(input('Enter Q for quit or any other key to compute tax '))
#     if sentinel == 'Q':
#         done = True
#         print(sentinel, done)
#         continue
#     else:
#         print('Compute tax')
#     price = float(input('What is the price? '))
#     tax = float(input('What is the tax rate? '))

#     calculated_price = price * (100 + tax) / 100
#     print(f'The calculated price is {calculated_price}')

# Scope = Local - Enclosing - Global - Builtin
# scoping.level.2.py
# test = 0 global scope
# def outer():
#     test = 1 outer scope
#     def inner():
#         test = 2 inner scope
#         print('inner:', test)
#     inner() function call
#     print('outer:', test)
# outer() function call
# print('global:', test)

# Argument passing
# key.points.argument.passing.py
# x = 3
# def func(y):
#     print(y)
# func(x) prints: 3

# key.points.assignment.py
# x = 3
# def func(x):
#     x = 7 defining a local x, not changing the global one
# func(x)
# print(x) prints: 3

# Change mutable object - List
# key.points.mutable.assignment.py
# x = [1, 2, 3]
# def func(x):
#     x[1] = 42 this change the original 'x' argument!
#     x = 'something else' this points x to a new string object
# func(x)
# print(x) still prints: [1, 42, 3]

# Positional Arguments
# arguments.positional.py
# def func(a, b, c):
#     print(a, b, c)
# func(1, 2, 3) prints: 1 2 3

# Keyword Arguments
# arguments.keyword.py
# def func(a, b, c):
#     print(a, b, c)
# func(a=1, c=2, b=3) prints: 1 3 2

# Iterable unpacking
# arguments.unpack.iterable.py
# def func(a, b, c):
#     print(a, b, c)
# values = (1, 3, -7)
# func(*values) equivalent to: func(1, 3, -7) and prints: (1, 3, -7)

# Dictionary unpacking
# arguments.unpack.dict.py
# def func(a, b, c):
#     print(a, b, c)
# values = {'b': 1, 'c': 2, 'a': 42}
# func(**values) equivalent to func(b=1, c=2, a=42) and prints: 42 1 2

# Mutable Defaults
# parameters.defaults.mutable.py
# def func(a=[], b{}):
#     print(a)
#     print(b)
#     print('#' * 12)
#     a.append(len(a)) this will affect a's default value
#     b[len(a)] = len(a) and this will affect b's one
# func()
# func()
# func()

# Returns
# return.single.value.py
# def factorial(n):
#     if n in (0, 1):
#         return 1
#     result = 2
#         for k in range(2, n): (start,stop)
#             print(f'(k{k})*(result{result})=')
#             result *= k assignment operator
#     return result
# f5 = factorial(5) f5 = 120
# print(f5)

# Multiple Returns
# return.multiple.py
# def moddiv(a, b):
#     return a // b, a % b floor div, modulus
# print(moddiv(20, 7)) prints (2,6)

# def getCharacter():
#     name = "Charmander"
#     hp = 40
#     cType = "Fire"
#     return name,hp,cType
# print(getCharacter())
# name,hp,cType = getCharacter()
# print('name:',name)
# print('hp:',hp)
# print('type:',cType)

# Return multiple
# values from a method using tuple
# This function returns a tuple
# def fun_test():
#     str = "polytechnic"
#     x = 9
#     return str, x Return tuple
# Driver code to test above method
# str, x = fun_test() Assign returned tuple
# # or x = fun_test()
# print(str)
# print(x)

# Lambdas [Functions]
# lambda.explained.py
# example 1: adder
# def adder(a, b):
#     return a + b
# is equivalent to:
# adder_lambda = lambda a, b: a + b
# example 2: to uppercase
# def to_upper(s):
#     return s.upper()
# is equivalent to:
# to_upper_lambda = lambda s: s.upper()