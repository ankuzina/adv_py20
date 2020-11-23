def swap(func):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return wrapper


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)