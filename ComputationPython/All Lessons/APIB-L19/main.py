# Types of http requests

# GET: The GET method requests a representation of the
# specified resource. Requests using GET should only
# retrieve data.
# POST: The POST method is used to submit an entity to
# the specified resource, often causing a change in state or
# side effects on the server.
# PUT: The PUT method requests that the target resource
# creates or updates its state with the state defined by the
# representation enclosed in the request.
# DELETE: The DELETE method requests that the target
# resource deletes its state.

# Type Hinting intro in v3.5

# fictitios langugage
# weakly typed
# a = 7
# b = "7"
# a + b == 14
# concatenate(a, b) == "77"

# a = 7
# a * 2 == 14
# a = "Hello";
# a * 2 == "HelloHello"

# True

# Hinting the data types in Python

# def greet(first_name: str, last_name: str, age: int = 18) -> str:
# return f"Greeting {first_name} {last_name} of age {age}"

# greet(123, 456, "hello)

# 'Greeting 123 456 of age hello'

# Typing module - support for type hints

# from typing import Optional
# def greet_again(name: Optional[str] = None):
# if name is not None:
# print(f"Hello {name}!")
# else:
# print("Hey dude")
# greet_again("john")

# class Cat:
# def __init__(self, name: str):
# self.name = name
# def call_cat(cat: Cat):
# return f"{cat.name}! Come here!"

# call_cat() function expects a cat argument,
# which should be an instance of Cat

# Working with requests module

# r = requests.get('https://api.github.com/user',
# auth=('user', 'pass'))
# r.headers['content-type'

# r = requests.get('https://api.github.com/user',
# auth=('user', 'pass'))
# r.encoding

# r.text

# r = requests.put('https://httpbin.org/put',
# data={'key': 'value'})
# r =
# requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')
# r

# r.json()

# r = requests.get('https://api.github.com/events')
# r.json()

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get',
# params=payload)
# print(r.url) see as url encoded

# r = requests.get('https://api.github.com/events',
# stream=True)

# r.raw
# r.raw.read(10)

# r = requests.get('https://httpbin.org/get')
# r.status_code

# url = 'https://httpbin.org/cookies'
# cookies = dict(cookies_are='working')

# r = requests.get(url, cookies=cookies)
# r.text

# s = requests.Session()
# s.get('https://httpbin.org/get')
