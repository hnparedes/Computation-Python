# @property decorator
# class property(fget=None, fset=None, fdel=None, doc=None)
# Returns a property attribute

# Kilometer with property class
# class Kilometer:
#     def __init__(self, speed=0):
#         self.speed = speed

#     def to_mph(self):
#         return(self.speed * 0.621371)

#     getter
#     def get_speed(self):
#       print('Getting value...')
#       return self._speed

#     setter
#     def set_speed(self, value):
#       print('Setting value...')
#       if value > 4520:
#          raise ValueError('speed above 4520 has never been achieved')
#          self._speed = value

# creating a property object
# speed = property(get_speed, set_speed)

# Before Property Decorator
# sedan = Kilometer(88)
# print(sedan.speed)
# print(sedan.to_mph())
# sedan.speed = 700
# print(sedan.__dict__['_speed'])

# Using @property decorator
# class Kiolometer:
#     def __init__(self, speed=0):
#         self.speed = speed

#     def to_mph(self):
#         return round((self.speed * 0.621371))

#     @property
#     def speed(self):
#       print('Getting value...')
#       return self._speed

#     @speed.setter
#     def speed(self, value):
#       print('Setting value...')
#       if value > 4520:
#          raise ValueError('speed above 4520 has never been achieved')
#          self._speed = value

# create an object
# sedan = Kiolometer(88)
# print(sedan.speed)
# print(sedan.to_mph())
# print('Converted is ',sedan.speed)
# print(sedan.__dict__)
# x15 = Kiolometer(4521)

# Iterables
# iterators/iterator.py
# class OddEven:
#     def __init__(self, data):
#         self._data = data
#         self.indexes = (list(range(0, len(data), 2)) + concatenates
#           list(range(1, len(data), 2)))
#         return print(self.indexes)

#     def __iter__(self): returns stream of data of iterator
#         return self
#
#     def __next__(self): returns the next item of the data stream
#         if self.indexes:
#             return self._data[self.indexes.pop(0)]
#         raise StopIteration prevents iteration going forever

# oddeven = OddEven('ThIsIsCoOl!')
# print(''.join(c for c in oddeven))
# oddeven = OddEven('Hello') or manually...
# it = iter(oddeven) this calls oddeven.__iter__ internally
# print(next(it)) H
# print(next(it)) l
# print(next(it)) o
# print(next(it)) e
# print(next(it)) l
