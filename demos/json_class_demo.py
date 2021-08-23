import json


class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]


# the json module cannot encode custom Python data types by default--it only works on most built-in types
# there is a way around this


class ComplexEncoder(json.JSONEncoder):
    """This is a subclass of the JSONEncoder class, it provides an alternate implementation (polymorphism)"""
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)


def imag_num_demo() -> complex:
    z = 3.0 + 8j  # j is an imaginary number
    print(type(z))  # <complex>
    print(complex(3, 8) == z)  # True
    print(complex(8, 3) == z)  # False

    # print(json.dumps(z))  # not serializable

    print(z.real)
    print(z.imag)

    return z


def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

"""
try:
    imaginary: complex = imag_num_demo()
    encode_complex(imaginary)
except TypeError:
    print("Uh oh, that wasn't a valid number!")
"""