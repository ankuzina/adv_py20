from itertools import starmap, product


def function(*args):
    s = 0
    for i in args:
        s += i ** 2
    return s


def maximize(lists, m):
    max = 0
    for item in starmap(function, list(product(*lists))):
        if item % m > max:
            max = item % m
    return max


lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, 1000))