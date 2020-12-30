import os, re
import threading
import time

def thread_job(i):
    global sum
    sum += i

m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2]
n = len(m)
print("dlina massiva =", n)
sum = 0
start = time.time()
threads = [threading.Thread(target=thread_job(m[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("summa =", sum)

finish = time.time()
vremya = finish - start
print("time1 = ", vremya)


m = [10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20]
n = len(m)
print("dlina massiva =", n)
sum = 0
start = time.time()
threads = [threading.Thread(target=thread_job(m[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("summa =", sum)

finish = time.time()
vremya = finish - start
print("time2 = ", vremya)


m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2]
n = len(m)
print("dlina massiva =", n)
sum = 0
start = time.time()
threads = [threading.Thread(target=thread_job(m[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("summa =", sum)

finish = time.time()
vremya = finish - start
print("time3 = ", vremya)


m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2]
n = len(m)
print("dlina massiva =", n)
sum = 0
start = time.time()
threads = [threading.Thread(target=thread_job(m[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("summa =", sum)

finish = time.time()
vremya = finish - start
print("time4 = ", vremya)