# 2 & 3.
class Ocean:
    def __init__(self, sea_creature_name, sea_creature_size):
        self.name = sea_creature_name
        self.size = sea_creature_size

    # placeholder
    def __str__(self):
        return f'The creature type is {self.name} and the size is {self.size}'

    # another placeholder
    def __repr__(self):
        return f'Ocean(\'{self.name}\', \'{self.size}\')'


c = Ocean('Jellyfish', '30 cm')
print(str(c))
print(repr(c))