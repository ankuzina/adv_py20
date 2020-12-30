import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker)
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("LIST = ", LIST, ", pustoy :(")



#ispravlenie


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker()) #worker() eto zhe funciya... skobochki!!
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("LIST = ", LIST) # ne pustoy