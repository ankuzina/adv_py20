import threading
import sys


def thread_job():
    global counter
    old_counter = counter
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
# 1 2 3 4 5 6 7 8 9 10 10 - vyvod

import threading
import random
import time
import sys


def thread_job():
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
# 1 2 3 4 5 6 7 4 3 1 1
# 1 2 3 4 5 6 7 7 2 5 5
# 1 2 3 4 5 6 7 5 6 6 6 - что-то не так с порядком вывода. когда программа (если конкретно - def thread_job()) "засыпает", различные потоки влияют на разные данные вывода,
# из-за чего мы получаем то, что получаем... неупорядоченный некорректный вывод. мне кажется, эту проблему можно решить следующим образом:
# сделать так, чтобы во время выполнения программы только один поток мог "работать". значит, надо сделать так, чтобы второй поток не начинал свою работу, пока её не закончит первый.

import threading
import random
import time
import sys


def thread_job():
    lock.acquire()  # mutex - тут добавили
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()
    lock.release() # а тут блокировка снимается


lock = threading.Lock()
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
# 1 2 3 4 5 6 7 8 9 10 10 - вот такой вывод