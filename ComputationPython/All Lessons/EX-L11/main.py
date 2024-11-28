# Errors vs Exceptions
# x = 0
# print('hello')
# def errr():
#     if x == 0:
#         raise ValueError('dont use zero')
#         print('this should come next')
#     errr()

# Try clause
# exceptions/try.syntax.py

# def try_syntax(numerator, denominator):
#     try:
#         print(f'In the try block:
# {numerator}/{denominator}')
#         result = numerator / denominator
#     except ZeroDivisionError as zde:
#         print(zde)
#     else:
#         print('The result is:', result)
#         return result
#     finally:
#         print('Exiting')

# print(try_syntax(12, 4))


# def try_syntax(numerator, denominator):
#     try:
#         print(f'In the try block: {numerator}/{denominator}')
#         result = numerator / denominator
#     except ZeroDivisionError as zde:
#         print(zde)
#     else:
#         print('The result is:', result)
#         return result
#     finally:
#         print('Exiting')


# print(try_syntax(11, 0))

# Try Try again
# exceptions/multiple.py
# values = (1, 0) # try (1, 0) and ('one', 2)

# try:
#     q, r = divmod(*values)
# except (ZeroDivisionError, TypeError) as e:
#     print(type(e),'--------', e)

# try:
#     q, r = divmod(*values)
# except ZeroDivisionError:
#     print("You tried to divide by zero!")
# except TypeError as e:
#     print(e)

# Raise exception within an except clause
# exceptions/replace.py
# class NotFoundError(Exception):
#     pass

# vowels = {'a': 1, 'e', 5, 'i':9, 'o': 15, 'u': 21}
# try:
#     pos = vowels['y'] try with 'a'
# except KeyError as e:
#     raise NotFoundError(*e.args) from None

# Using with as try finally
# my_file = open("hola.txt", mode="wt")
# try:
#     my_file.write("Greetings!\n")
# finally:
#     my_file.close()
