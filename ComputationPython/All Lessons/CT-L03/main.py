# year = 2023
# print ("Hello World!")
# print (”AI changed a lot in %d." % (year))

# Basic If Else
# ternary operator
# color = 'red'
# new_value = 'blue' if color == 'red' else 'white'
# print(f'new color is {new_value}')
# conditional.2.py
# late = False
# if late:
# print('I need to call my manager!')
# else:
# print('no need to call my manager...')
# ternary.py
# ternary operator
# order_total = 75
# discount = 25 if order_total > 100 else 0
# print(order_total, discount)

# Elif Clause
# taxes.py
# income = 15000
# if income < 10000:
# tax_coefficient = 0.0 #1
# elif income < 30000:
# tax_coefficient = 0.2 #2
# elif income < 100000:
# tax_coefficient = 0.35 #3
# else:
# tax_coefficient = 0.45 #4
# print(f'You will pay: ${income *
# tax_coefficient} in taxes')

# Repeating execution of a code block
# word=‘polytechnic’
# for letter in word:
# print (letter)

# some_set = {'red', 'blue', 'green'}
# for color in some_set:
# print(color.upper())

# for number in [0, 1, 2, 3, 4]:
# print(number)

# for number in range(5):
# print(number)

# list(range(10)) # one value: from 0 to
# value (excluded)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(3, 8)) # two values: from
# start to stop
# [3, 4, 5, 6, 7]

# For loops
# surnames = ['Rivest', 'Shamir', 'Adleman']
# for position in range(len(surnames)):
# print(position, surnames[position])

# Better code
# surnames = ['Rivest', 'Shamir', 'Adleman']
# for surname in surnames:
# print(surname)

# surnames = ['Rivest', 'Shamir', 'Adleman']
# for position, surname in enumerate(surnames):
# print(position, surname)

# For Loop with Zip
# multiple.sequences.explicit.py
# people = ['Nick', 'Rick', 'Roger', 'Syd’] # list
# ages = [23, 24, 23, 21]  # list
# instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']
# for person, age, instrument in zip(people, ages, instruments):
#     print(person, age, instrument)

# could be rewritten to manually break apart tuple
# multiple.sequences.explicit.py
# people = ['Nick', 'Rick', 'Roger', 'Syd']
# ages = [23, 24, 23, 21]
# instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']
# for person, age, instrument in zip(people, ages, instruments):
# print(person, age, instrument)

# vs

# multiple.sequences.implicit.py
# people = ['Nick', 'Rick', 'Roger', 'Syd']
# ages = [23, 24, 23, 21]
# instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']
# for data in zip(people, ages, instruments):
# person, age, instrument = data
# print(person, age, instrument)

# While loop with reverse method
# binary.py
# n = 39
# remainders = [] # List
# while n > 0: # Modulus
#     remainder = n % 2  # remainder of division by 2
# remainders.append(remainder)  # keep track of
# remainders
#     n //= 2  # divide n by 2
#     print(n)
# remainders.reverse()
# print(remainders)

# Break and Continue
# any.py
# items = [0, None, 0.0, True, 0, 7] # True and 7 evaluate
# to True
# found = False # this is called "flag"
# for item in items:
# print('scanning item', item)
# if item:
# found = True # we update the flag
# break
# if found: # we inspect the flag
# print('At least one item evaluates to True')
# else:
# print('All items evaluate to False')

# Walrus Operator
# walrus.if.py
# if remainder := value % modulus:
# print(f"Not divisible! The remainder is
# {remainder}.")

# Compare with Assignment Operator
# menu.no.walrus.py
# flavors = ["pistachio", "malaga", "vanilla",
#            "chocolate", "strawberry"]
# prompt = "Choose your flavor: "
# print(flavors)
# while True:
#     choice = input(prompt)
# if choice in flavors:
#     break
# print(f"Sorry, '{choice}' is not a valid option.")
# print(f"You chose '{choice}'.")

# vs

# menu.walrus.py
# flavors = ["pistachio", "malaga", "vanilla",
# "chocolate", "strawberry"]
# prompt = "Choose your flavor: "
# print(flavors)
# while (choice := input(prompt)) not in flavors:
# print(f"Sorry, '{choice}' is not a valid option.")
# print(f"You chose '{choice}'.")

# itertools - Functions creating iterators fro efficient looping
# from itertools import permutations
# abc = list(permutations('secret123’))
# len(abc)
# or print(abc)

# from itertools import permutations
# print(list(permutations('abcd', 2))

# Be careful with imports
# from turtle import *
# from math import *
# print(*dir()) # prints all functions & var
# radians(360)