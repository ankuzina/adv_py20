import itertools


def compress_string(s):
    m = []
    for key, value in itertools.groupby(s):
        m.append((len(list(value)), key))
    return m