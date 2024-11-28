# C code
# int x = 4;

# python code
# X = 4

# Immuatable
# age = 42
# age
# 42
# age = 43 #A
# age
# 43

# Really Immutable
# age = 42
# id(age)
# 4377553168
# age = 43 A
# id(age)
# 4377553200

# Integers as immutable objects
# a = 14
# b = 3
# a + b
# 17
# a * b
# int(1.75)
# 1
# int(-1.75)
# -1
# int('10110', base=2)

# Boolean
# int(True)
# 1
# int(False)
# 0
# bool(1)
# True
# bool(-42)
# True
# bool(0)
# False
# not True
# False
# not False
# True
# True and True
# True
# False or True
# True

# Floating point numbers
# (.3 - .1) * 2
# 0.39999999999997

# Decimal
# from decimal import *
# getcontext().prec = 3
# Decimal(1) / Decimal(7)
# Decimal('0.143')

# Strings and Bytes
# str1 = 'This is a string'
# str2 = "This is also a string"
# str3 = "'This is built with,
# ... so it can span multiple lines.'"

# str4 = """This too
# ... is a multiline"""

# str4 #A
# 'This too\nis a multiline'

# print(str4)
# This too
# is a multiline

# Encoding and Decoding
# s = "This is unic0de"
# type(s)
# <class 'str'>
# encoded_s = s.encode('utf-8')
# type(encoded_s)
# <class 'bytes'>
# bytes_obj = b"A bytes object"
# type(bytes_obj)
# <class 'bytes'>
# print(bytes_obj)
# b'A bytes object'

# Indexing and Slicing
# s = "The trouble is you think you have time."
# s[0] # indexing at position 0
# 'T'
# s[5] # indexing at position 5
# 'r'
# s[:4] # slicing, only the stop position
# 'The'
# s[4:] # slicing, only the start position
# 'trouble is you think you have time.'
# s[2:14] # slicing, both start and stop
# 'e trouble is'
# s[2:14:3] # start, stop and step (every 3 chars)
# 'erb'

# Tuples are immutable
# t = () # empty tuple
# type(t)
# <class 'tuple'>
# one_element_tuple = (42, ) # you need the comma!
# three_elemets_tuple = (1, 3, 5) # Parentheses are optional
# a, b, c = 1, 2, 3 # tuple for multiple assignment
# a, b, c # implicit tuple to print with one instruction
# (1, 2, 3)
# 3 in three_elemets_tuple # membership test
# True

# Lists are mutable sequences
# [] # empty list
# []
# list() # same as []
# []
# [1, 2, 3] # as with tuples, items are comma separated
# [1, 2, 3]
# [x + 5 for x in [2, 3, 4]] # Python is magic
# [7, 8, 9]
# list((1, 3, 5, 7, 9)) # list from a tuple
# [1, 3, 5, 7, 9]
# list('hello') # list from a string
# ['h', 'e', 'l', 'l', 'o']

# Manipulating Lists
# a = [1, 2, 1, 3]
# a.append(13) # append anything at the end
# a
# [1, 2, 1, 3, 13]
# a.count(1) # how many `1s` a in the list?
# 2
# a.extend([5, 7]) # extend by another (or seq)
# a
# [1, 2, 1, 3, 13, 5, 7]
# a.index(13) # position of `13`
# 4
# a.insert(0, 17) # insert `17` at position 0
# a
# [17, 1, 2, 1, 3, 13, 5, 7]
# a.pop() # pop (remove and return) last
# element
# 7
# a.pop(3) # pop element at position 3
# 1
# a
# [17, 1, 2, 3, 13, 5]
# a.remove(17) # remove `17` from the list
# a
# [1, 2, 3, 13, 5]
# a.reverse() # reverse the order of the
# elements
# a
# [5, 13, 3, 2, 1]
# a.sort() # sort the list
# a
# [1, 2, 3, 5, 13]
# a.clear() # remove all elements from the list
# a
# []

# Other List methods
# a = list('hello') # makes a list from a string
# a
# ['h', 'e', 'l', 'l', 'o']
# a.append(100) # append 100, heterogeneous type
# a
# ['h', 'e', 'l', 'l', 'o', 100]
# a.extend((1, 2, 3)) # extend using tuple
# a
# ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]
# a.extend('...') # extend using string
# a
# ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']

# Mapping type: Dictionaries (mutable)
# a = dict(A=1, Z=-1)
# b = {'A': 1, 'Z': -1}
# c = dict(zip(['A', 'Z'], [1, -1]))
# d = dict([('A', 1), ('Z', -1)])
# e = dict({'Z': -1, 'A': 1})
# a == b == c == d == e # tests if same?
# True # They are indeed

# Zip
# list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5]))
# [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
# list(zip('hello', range(1, 6))) # equivalent, more pythonic
# [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]

# Square bracket for Dictionary Key
# d = {}
# d['a'] = 1  # let's set a couple of (key, value) pairs
# d['b'] = 2
# len(d)  # how many pairs?
# 2
# d['a']  # what is the value of 'a'?
# 1
#  d  # view d
# {'a': 1, 'b': 2}
# del d['a']  # remove `a`
# d
# {'b': 2}
# d['c'] = 3  # add 'c': 3
# 'c' in d  # membership is checked against the keys
# True
# 3 in d  # not the values
# False
# 'e' in d
# False
# d.clear()  # clean up dictionary
# d
# {}
