import operator
from functools import reduce


def prod(iterator):
    return reduce(operator.mul, iterator, 1)


print(prod([7, 8, 9]))
