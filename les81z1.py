def print_map(function, iterable):
    i = iter(iterable)
    while i < iterable:
        print(function(next(i)))