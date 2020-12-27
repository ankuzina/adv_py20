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
# 1 2 3 4 5 6 7 5 6 6 6 - ���-�� �� ��� � �������� ������. ����� ��������� (���� ��������� - def thread_job()) "��������", ��������� ������ ������ �� ������ ������ ������,
# ��-�� ���� �� �������� ��, ��� ��������... ��������������� ������������ �����. ��� �������, ��� �������� ����� ������ ��������� �������:
# ������� ���, ����� �� ����� ���������� ��������� ������ ���� ����� ��� "��������". ������, ���� ������� ���, ����� ������ ����� �� ������� ���� ������, ���� � �� �������� ������.

import threading
import random
import time
import sys


def thread_job():
    lock.acquire()  # mutex - ��� ��������
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()
    lock.release() # � ��� ���������� ���������


lock = threading.Lock()
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
# 1 2 3 4 5 6 7 8 9 10 10 - ��� ����� �����