def map1(a, iterable):
    for i in iterable:
        yield a(i)

def enumerate1(iterable, s = 0):
    for i in iterable:
        yield s, i
        s += 1

def zip1(*vals):
    n = len(vals[0])
    for i in range(n):
        arr = []
        for p in vals:
            arr.append(p[i])
        yield list(arr)