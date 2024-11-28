# Filter Function - None
# filter_none.py
# test [2, 5, 8, 0, 0, 1, 0]
# list(filter(None, test))

# List Comprehensions [expression for clause]
# squares.for.py
# squares = []
# for n in range(10);
#     squares.append(n ** 2)
# squares

# vs

# squares.comprehension.py
# [n ** 2 for n in range(10)]

# List Comprehensions
# co = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#         co.append((x, y))
# co

# vs

# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# tuples must be parenthesized
# [(x, x**2) for x in range(6)]

# list_comprehension squares
# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]
# print(*squares, sep="\n")

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# squares = {key: value**2 for key, value in
# my_dict.items()}
# print(squares)

# Normal Function vs List Comprehension
# function loop
# def is_greater_than_x(some_list, threshold):
#     result = []
#     for ele in some_list:
#         result.append(ele > threshold)
#     return result
#
# is_greater_than_x([99, 55, 69, 88], 70) some_list, threshold

# vs

# def is_greater_than_x(some_list, threshold):
#     return [ ele > threshold for ele in some_list ]
#
# is_greater_than_x([99, 55, 69, 88], 70) some_list, threshold
