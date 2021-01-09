# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice


class Enemy(Attacker):
    pass


def generate_random_dragon():
    RandomEnemyType = choice(dragon_types)
    enemy = RandomEnemyType()
    return enemy


def generate_random_mid_dragon():
    RandomEnemyTypemid = choice(dragon_mid_types)
    enemymid = RandomEnemyTypemid
    return enemymid


def generate_random_hard_dragon():
    RandomEnemyTypehard = choice(dragon_hard_types)
    enemyhard = RandomEnemyTypehard
    return enemyhard


def generate_random_troll():
    RandomEnemyType = choice(troll_types)
    enemy = RandomEnemyType()
    return enemy


def generate_random_mid_troll():
    RandomEnemyTypemid = choice(troll_mid_types)
    enemymid = RandomEnemyTypemid
    return enemymid


def generate_random_hard_troll():
    RandomEnemyTypehard = choice(troll_hard_types)
    enemyhard = RandomEnemyTypehard
    return enemyhard


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_dragon() for i in range(enemy_number)]
    return enemy_list


def generate_mid_dragon_list(enemy_number):
    mid_enemy_list = [generate_random_mid_dragon() for i in range(enemy_number)]
    return mid_enemy_list


def generate_hard_dragon_list(enemy_number):
    hard_enemy_list = [generate_random_hard_dragon() for i in range(enemy_number)]
    return hard_enemy_list


def generate_troll_list(enemy_number):
    enemy_list = [generate_random_troll() for i in range(enemy_number)]
    return enemy_list


def generate_mid_troll_list(enemy_number):
    mid_enemy_list = [generate_mid_troll_list() for i in range(enemy_number)]
    return mid_enemy_list


def generate_hard_troll_list(enemy_number):
    hard_enemy_list = [generate_hard_troll_list() for i in range(enemy_number)]
    return hard_enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class Troll(Enemy):
    def set_answer(self, answer):
        # print(answer)
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 500
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(max(x, y)) + '-' + str(min(x, y))
        self.set_answer(max(x, y) - min(x, y))
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class GrayTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 20
        self._color = 'серый'

    def question(self):
        number = randint(1, 10)
        self.__quest = 'Угодай часлу ат 1 да 10'
        self.set_answer(str(number))
        return self.__quest


class BlueTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'голубой'

    def prost(self):
        np = [1]
        p = []
        for i in range(2, 100):
            if not i in np:
                p += [i]
                for j in range(2 * i, 100, i):
                    np += [j]
        return p

    def question(self):
        number = randint(1, 100)
        self.__quest = str(number) + ' прастая числа? (да/нет)'
        self.set_answer('да' if number in self.prost() else 'нет')
        return self.__quest


class PinkTroll(Troll):
    def __init__(self):
        self._health = 300
        self._attack = 10
        self._color = 'розовый'

    def prost(self):
        np = [1]
        p = []
        for i in range(2, 100):
            if not i in np:
                p += [i]
                for j in range(2 * i, 100, i):
                    np += [j]
        return p

    def delit(self, number):
        result = []
        for i in self.prost():
            while number % i == 0:
                result += [i]
                number /= i
        return ', '.join(list(map(str, result)))

    def question(self):
        number = randint(1, 100)
        self.__quest = str(number) + ' разлажы на прастыи (через запятую по возрастанию. пример:2, 2, 3)'
        self.set_answer(self.delit(number))
        return self.__quest


class GreenDragonmid(Dragon):
    def __init__(self):
        self._health = 500
        self._attack = 50
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 1000)
        y = randint(1, 1000)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragonmid(Dragon):
    def __init__(self):
        self._health = 500
        self._attack = 50
        self._color = 'красный'

    def question(self):
        x = randint(1, 1000)
        y = randint(1, 1000)
        self.__quest = str(max(x, y)) + '-' + str(min(x, y))
        self.set_answer(max(x, y) - min(x, y))
        return self.__quest


class BlackDragonmid(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 25
        self._color = 'чёрный'

    def question(self):
        x = randint(1, 50)
        y = randint(1, 50)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class GreenDragonhard(Dragon):
    def __init__(self):
        self._health = 1000
        self._attack = 50
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 10000)
        y = randint(1, 10000)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragonhard(Dragon):
    def __init__(self):
        self._health = 500
        self._attack = 50
        self._color = 'красный'

    def question(self):
        x = randint(1, 10000)
        y = randint(1, 10000)
        self.__quest = str(max(x, y)) + '-' + str(min(x, y))
        self.set_answer(max(x, y) - min(x, y))
        return self.__quest


class BlackDragonhard(Dragon):
    def __init__(self):
        self._health = 500
        self._attack = 50
        self._color = 'чёрный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class GrayTrollmid(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 20
        self._color = 'серый'

    def question(self):
        number = randint(1, 20)
        self.__quest = 'Угодай часлу ат 1 да 20'
        self.set_answer(str(number))
        return self.__quest


class BlueTrollmid(Troll):
    def __init__(self):
        self._health = 400
        self._attack = 25
        self._color = 'голубой'

    def prost(self):
        np = [1]
        p = []
        for i in range(2, 1000):
            if not i in np:
                p += [i]
                for j in range(2 * i, 1000, i):
                    np += [j]
        return p

    def question(self):
        number = randint(1, 100)
        self.__quest = str(number) + ' прастая числа? (да/нет)'
        self.set_answer('да' if number in self.prost() else 'нет')
        return self.__quest


class PinkTrollmid(Troll):
    def __init__(self):
        self._health = 300
        self._attack = 25
        self._color = 'розовый'

    def prost(self):
        np = [1]
        p = []
        for i in range(2, 1000):
            if not i in np:
                p += [i]
                for j in range(2 * i, 1000, i):
                    np += [j]
        return p

    def delit(self, number):
        result = []
        for i in self.prost():
            while number % i == 0:
                result += [i]
                number /= i
        return ', '.join(list(map(str, result)))

    def question(self):
        number = randint(1, 100)
        self.__quest = str(number) + ' разлажы на прастыи (через запятую по возрастанию. пример:2, 2, 3)'
        self.set_answer(self.delit(number))
        return self.__quest


class GrayTrollhard(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'серый'

    def question(self):
        number = randint(1, 50)
        self.__quest = 'Угодай часлу ат 1 да 50'
        self.set_answer(str(number))
        return self.__quest


class BlueTrollhard(Troll):
    def __init__(self):
        self._health = 400
        self._attack = 25
        self._color = 'голубой'

    def prost(self):
        np = [1]
        p = []
        for i in range(2, 1000):
            if not i in np:
                p += [i]
                for j in range(2 * i, 1000, i):
                    np += [j]
        return p

    def question(self):
        number = randint(1, 100)
        self.__quest = str(number) + ' прастая числа? (да/нет)'
        self.set_answer('да' if number in self.prost() else 'нет')
        return self.__quest


class PinkTrollhard(Troll):
    def __init__(self):
        self._health = 600
        self._attack = 50
        self._color = 'розовый'

    def prost(self):
        np = [1]
        p = []
        for i in range(2, 10000):
            if not i in np:
                p += [i]
                for j in range(2 * i, 10000, i):
                    np += [j]
        return p

    def delit(self, number):
        result = []
        for i in self.prost():
            while number % i == 0:
                result += [i]
                number /= i
        return ', '.join(list(map(str, result)))

    def question(self):
        number = randint(1, 100)
        self.__quest = str(number) + ' разлажы на прастыи (через запятую по возрастанию. пример:2, 2, 3)'
        self.set_answer(self.delit(number))
        return self.__quest


dragon_types = [GreenDragon, RedDragon, BlackDragon]
dragon_mid_types = [GreenDragonmid, RedDragonmid, BlackDragonmid]
dragon_hard_types = [GreenDragonhard, RedDragonhard, BlackDragonhard]
troll_types = [GrayTroll, BlueTroll, PinkTroll]
troll_mid_types = [GrayTrollmid, BlueTrollmid, PinkTrollmid]
troll_hard_types = [GrayTrollhard, BlueTrollhard, PinkTrollhard]