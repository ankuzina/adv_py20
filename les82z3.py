import itertools


def get_combinations(s, k):
    m = []
    for i in range(1, k+1):
        m.append(list(itertools.combinations(s, i)))
    return m