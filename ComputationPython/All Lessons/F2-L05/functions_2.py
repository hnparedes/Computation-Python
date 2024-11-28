# Question 1 & 2
# a, b, c, d = [1, 2, 3, 4]

# Question 3
# unpacking_operator.py
# a_tuple = (1, 2, 3, 4, 5, 6, 7)
# a_list = [22, 33, 44, 55]


# def some_dict():
#     a_dict = {'abe': 123, 'doe': 345, 'ken': 789}
#     return a_dict


# print(*a_tuple)
# print(*a_list)
# print(*some_dict().items())

# Question 4
# hp_damage = lambda h, dmg: h - dmg

# damage = 20
# hp = 100

# print(f'Your character took {damage} points of damage')
# print(f'Your character has dropped from {hp} hit points to {hp_damage(hp, damage)} hit points available')

# Question 5
"""
    Converts a given score ("Great", "Ok", or "Poor") into a numerical value.

    Parameters:
    score (str): The score input as "Great", "Ok", or "Poor".

    Returns:
    int: A numerical value based on the score.
         - "Great" returns 10
         - "Ok" returns 5
         - "Poor" returns 3
"""


def scoretonumber(score):

    score = str.upper(score)
    result = 0
    first = score[0]
    if first == "G":
        result = 10
    elif first == "O":
        result = 5
    elif first == "P":
        result = 3
    return result


"""
    The main function that prompts the user to input three scores and calculates the maximum score and average score.

    Prompts:
    - Enter score 1 as Great, Ok, or Poor
    - Enter score 2 as Great, Ok, or Poor
    - Enter score 3 as Great, Ok, or Poor

    Computes:
    - Maximum of the three scores.
    - Average of the three scores on a 1-10 scale.

    Prints:
    - The maximum score.
    - The average score rounded to 2 decimal places.
"""


def main():
    score1 = input('Enter score 1 as Great, Ok or Poor: ')
    score2 = input('Enter score 2 as Great, Ok or Poor: ')
    score3 = input('Enter score 3 as Great, Ok or Poor: ')
    x1 = scoretonumber(score1)
    x2 = scoretonumber(score2)
    x3 = scoretonumber(score3)
    xmax = max(x1, x2, x3)
    some_avg = (x1 + x2 + x3) / 3
    print(f'The maximum score was {xmax}')
    print(f'The avg score on 1-10 scale would have been {round(some_avg, 2)}')


main()
