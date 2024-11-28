# Question 3
# a = 7
# print(id(a))
# a = 5
# print(id(a))
# a = 7
# b = a
# print(id(b))

# Question 4
# print(int('abcdef0', 16))

# Question 5
# b = int(False)
# b += 1
# print(b)

# Question 6
# some_string = "Polytechnic is the best STEM school in Florida"
# print(some_string[19:35:2])

# Question 7
# some_collection = ()
# print(type(some_collection))

# Question 8
# abe = [1, 2, 3]
# print(type(abe))
# lincoln = list(abe)
# print(type(lincoln))

# Question 9
# c = []
# c.append(42)
# c.append(99)
# c.pop(0)
# print(c)

# Question 10
# grades = {'mary': 99, 'patya': 87, 'jose': 47}
# choice = input('Type S to start ')
# choice = choice.upper()
# if choice == "S":
#     average_grade = int(sum(grades.values()) / len(grades))
#     print('The average grade is', str(average_grade))
#     for name in sorted(grades):
#         print('%s: %s' % (name, grades[name]))

# Question 11

# school_name = input("Please enter only upper case letters for school name ").upper()
# print(school_name)
# print("I see you")

# Question 12


# def fun_test():
#     str = 'polytechnic'
#     x = 9
#     j = 54
#     k = 'stem'
#     return str, x


# str, x = fun_test()
# x = fun_test()
# print(str)

# Question 13

# d = {}
# d['red'] = 'rojo'
# d['blue'] = 'azul'
# print('blue' in d)

# Question 14
# print(list(range(1000)))

# Question 15
for number in range(20):
    print(number)
