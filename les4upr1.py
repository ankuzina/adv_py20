def fib(n):
    fib1 = fib2 = 1
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2

import sys
if __name__ == "__main__":
    if len(sys.argv) >= 1:
        if sys.argv[1] == "-n":
            print(str(fib(int(sys.argv[2]))))
        else:
            print(str(fib(int(sys.argv[1]))))