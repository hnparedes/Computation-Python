# Base64 Encoding

# import base64
# str_ = "AB"
# str_bytes = str_.encode("ascii")
# b64_bytes = base64.b64encode(str_bytes)
# new64_string = b64_bytes.decode("ascii")
# print(f"New encoded string: {new64_string}")

# Hashlib module is part of standard library
# import hashlib
# check which algo are available
# hashlib.algorithms_available

# Testing hashlib
# import hashlib
# h = 'professor'
# h = hashlib.new('md5', h.encode('UTF-8')).hexdigest()
# h = hashlib.new('md5', b'professor').hexdigest()
# print(f'hash is {h}')

# hash is
# 3f9cd3c7b11eb1bae99dddb3d05da3c5

# SHA-1
# import hashlib
# h = 'professor'
#  h = hashlib.new(‘sha256', h.encode('UTF-8')).hexdigest()
# h = hashlib.new(‘sha256', b'professor').hexdigest()
# print(f'hash is {h}')

# hash is
# 17c1532ca6cff8f6a3a8200028af6c2580bf37f39e10cb0966e8a573e3b24a1f

# Cracking hashes
#  import hashlib
# h = ‘key'
# h = hashlib.new('md5', h.encode('UTF-8')).hexdigest()
#  h = hashlib.new('md5', b’key').hexdigest()
#  print(f'hash is {h}')

# hash is 3c6e0b8a9c15224a8228b9a98ca1531d

# JSON Web Tokens
# jwt/tok.py
# import jwt
# data = {'payload': 'data', 'id': 123456789}
# token = jwt.encode(data, 'secret-key')
# print(f'The token is \n{token}\n')
# algs = ['HS256', 'HS512']
# data_out = jwt.decode(token, 'secret-keyxxxx', algorithms=algs)
# print(data_out)
