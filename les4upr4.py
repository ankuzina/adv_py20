# coding=UTF-8
from time import time
import os


def decorator_maker(p):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            file = open(p, "w")
            t1 = time()
            s = func(*args, **kwargs)
            t2 = time()
            file.write(str(t1) + "\n")
            file.write(','.join(args))
    #        file.write(','.join(kwargs)) #распечатать словарь
            file.write(str(s) + '\n')
            file.write(str(t2) + "\n")
            twork = t2 - t1
            file.write(str(twork) + "\n")
            file.close()
            return s
        return wrapper
    return my_decorator

p = os.path.abspath('file44.txt')
@decorator_maker(p)
def hello():
    return 0

if __name__ == '__main__':
    hello()
    file = open(p, "r")
    print(file.read())
    file.close()
