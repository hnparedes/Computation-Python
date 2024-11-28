# Question 1
# @some_process
# def func(arg1, arg2, ...):
#     pass

# Question 4
# class Alien:
#     species = "ET"

# print(Alien.species)

# Question 10
# def try_syntax(numerator, denominator):
#     try:
#         print(f'In the try block: {numerator}/{denominator}')
#         result = numerator / denominator

#      except ZeroDivisionError as zde:
#         print(zde)

#     else:
#         print('The result is:', result)
#         return result

#     finally:
#         print('Exiting')
# print(try_syntax(12, 4))
# print(try_syntax(11, 0))
# print('this is after exception')

# Question 12
# filename = input("Enter filename: ")

# outfile = open(filename, "w")

# content_ = "This is a test\n"

# outfile.write(content_)

# outfile.close()

# Question 13
import json
info = {
    'full_name': 'Sherlock Holmes',
    'address': {
        'street': '221B Baker St',
        'zip': 'NW1 6XE',
        'city': 'London',
        'country': 'UK',
    }
}
print(json.dumps(info, indent=2, sort_keys=True))
