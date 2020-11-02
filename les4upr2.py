def chetnost(list_):  # числа вводятся через пробел в одну строку
    s = 0
    for i in range(len(list_)):
        if (list_[i] ) %2 == 0: # проверка на чётность
            s += 1
    return s


def decorator(func):
    def wrapper(list_):
        s = func(list_)
        if s == 0:
            return "Net("
        elif s >= 10:
            return "Slishkom mnogo"
    return wrapper


if __name__ == '__main__':
    massiv = list(map(int, input().split()))
    print(chetnost(massiv))
    print(decorator(chetnost)(massiv))