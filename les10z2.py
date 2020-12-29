import os, re
import threading
import random
import time
import sys


def thread_job(suffix):
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # poluchenie verdikta
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

start = time.time()

lock = threading.Lock()

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

threads = [threading.Thread(target=thread_job,args=(_,)) for _ in range(20,30)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

finish = time.time()
vremya = finish - start
print("time1 = ", vremya)


received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

start = time.time()
for suffix in range(20, 30):
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
finish = time.time()
vremya = finish - start
print("time2 = ", vremya)