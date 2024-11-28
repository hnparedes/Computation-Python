# 1abc

# import hashlib

# original_hash = 'd077f244def8a70e5ea758bd8352fcd8'

# for letter in 'abcdefghijklmnopqrstuvwxyz':
#     best_guess = 'ca' + letter
#     h = hashlib.new('md5', best_guess.encode('UTF8')).hexdigest()

#     if h == original_hash:
#         print(f"Correct word is: {best_guess}")
#         break
#     else:
#         print(f"Checked {best_guess}, hash: {h}")

letters = 'ca'
for letter1 in letters:
    for letter2 in letters:
        xx = letter1 + letter2
        print(xx)
