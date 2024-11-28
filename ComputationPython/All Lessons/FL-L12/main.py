# Opening Files

# Ok
# files/open_try.py
# da = open('dadams.txt', 'rt') r: read, t: text
# for line in da.readlines():
# print(line.strip()) remove whitespace and
# print
# da.close()

# Better
# files/open_try.py
# da = open('dadams.txt') rt is default
# try:
# for line in da: we can iterate directly on
# da
# print(line.strip())
# finally:
# da.close()

# Best way to do it
# files/open_with.py
# with open('dadams.txt') as da:
# for line in da:
# print(line.strip())

# Writing files

# files/print_file.py
# with open('print_example.txt', 'w') as fw:
# print('Hey I am printing into a file!!!',
# file=fw)

# files/read_write.py
# with open('dadams.txt') as f:
# lines = [line.rstrip() for line in f
# with open('dadams_copy.txt', 'w') as fw:
# fw.write('\n'.join(lines))

# Reading Binary files

# Specify the size of each chunk to read
# chunk_size = 16
# with open('ComputerScience64.jpg', 'rb') as file_:
# Using while loop to iterate the file data
# while True:
# chunk = file_.read(chunk_size)
# if not chunk:
# break
# Processing the chunk of binary data
# print(f'Read {len(chunk)} bytes: {chunk}')

# files/read_write_bin.py
# with open('example.bin', 'wb') as fw:
# fw.write(b'This is binary data...')
# with open('example.bin', 'rb') as f:
# print(f.read()) prints: b'This is binary data...'

# Protect against overwriting

# files/write_not_exists.py
# with open('write_x.txt', 'x')
# as fw: this succeeds
# fw.write('Writing line 1')
# with open('write_x.txt', 'x')
# as fw: this fails
# fw.write('Writing line 2')

# Import pathlib module

# files/existence.py
# from pathlib import Path
# p = Path('fear.txt')
# path = p.parent.absolute()
# print(p.is_file()) True
# print(path) /Users/something
# print(path.is_dir()) True
# q = Path('/Users/cnavarro/Documents')
# print(q.is_dir()) True

# Working with JavaScript Object Notation

# json_examples/json_basic.py
# import sys
# import json
# data = {
# 'big_number': 2 ** 3141,
# 'max_float': sys.float_info.max,
# 'a_list': [2, 3, 5, 7],
# }
# json_data = json.dumps(data)
# data_out = json.loads(json_data)
# assert data == data_out json and back,
# data matches
# test if True, if not, False raises an AssertionError.
# print(f'all output: {data_out} \n')
# print(json.dumps(data, indent=2,
# sort_keys=True))

# In-memory IO stream

# io_examples/string_io.py
# import io
# with io.StringIO() as stream:
# stream.write('Learning Python
# Programming.\n')
# print('Become a Python ninja!',
# file=stream)
# contents = stream.getvalue()
# print(contents)

# HTTP get requests

# python -m pip install requests
# io_examples/reqs.py
# import requests
# urls = {
# "get":
# "https://httpbin.org/get?t=learn+python+programming",
# "headers": "https://httpbin.org/headers",
# "ip": "https://httpbin.org/ip",
# "user-agent": "https://httpbin.org/user-agent",
# "UUID": "https://httpbin.org/uuid",
# "JSON": "https://httpbin.org/json",
# }
# def get_content(title, url):
# resp = requests.get(url)
# print(f"Response for {title}")
# print(resp.json())
# for title, url in urls.items():
# get_content(title, url)
# print("-" * 40)

# HTTP post requests

# python -m pip install pprint
# io_examples/reqs_post.py
# import requests, pprint
# url = 'https://httpbin.org/post'
# data = dict(title='Learn Python Programming')
# resp = requests.post(url, data=data)
# print('Response for POST')
# pprint.pprint(resp.json(),width=-1)

# Python pickle

# Only unpickle data you trust.
# persistence/pickler.py
# import pickle
# from dataclasses import dataclass
# @dataclass
# class Person:
# first_name: str
# last_name: str
# id: int
# def greet(self):
# print(f'Hi, I am {self.first_name} {self.last_name}'
# f' and my ID is {self.id}')
# people = [
# Person('Obi-Wan', 'Kenobi', 123),
# Person('Anakin', 'Skywalker', 456),
# ]
# # save data in binary format to a file
# with open('data.pickle', 'wb') as stream:
# pickle.dump(people, stream)
# # load data from a file
# with open('data.pickle', 'rb') as stream:
# peeps = pickle.load(stream)
# for person in peeps:
# person.greet()

# Python shelve

# persistence/shelf.py
# import shelve
# class Person:
# def __init__(self, name, id):
# self.name = name
# self.id = id
# with shelve.open('shelf1.shelve') as db:
# db['obi1'] = Person('Obi-Wan', 123)
# db['ani'] = Person('Anakin', 456)
# db['a_list'] = [2, 3, 5]
# db['delete_me'] = 'we will have to delete this’
# print(list(db.keys())) 'ani', 'delete_me’, ...
# del db['delete_me'] gone!
# print(list(db.keys())) ['ani', 'a_list', 'obi1']
# print('delete_me' in db) False
# print('ani' in db) True
# a_list = db['a_list']
# a_list.append(7)
# db['a_list'] = a_list
# print(db['a_list']) [2, 3, 5, 7]
