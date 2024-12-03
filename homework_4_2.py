import itertools


def generate_infinite_numbers():
    for number in itertools.count(0):
        yield number


def apply_function(func, iterator):
    return map(func, iterator)


def combine_iterators(*iterators):
    return itertools.chain(*iterators)
