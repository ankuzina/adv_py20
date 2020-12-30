def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

n = int(input())
for fib in fibonacci(n):
    print(fib, end=' ')
print()

for fib in fibonacci(10):
    print(fib, end=' ')
print()

for fib in fibonacci(20):
    print(fib, end=' ')
print()