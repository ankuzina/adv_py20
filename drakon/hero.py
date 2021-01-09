# coding: utf-8
# license: GPLv3
from gameunit import *

# FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.
"""


class Hero(Attacker):
    _health = 100
    _attack = 200
    _experience = 18
    _lvl = 1
    _importance = 2

    def __init__(self, name):
        self._name = name

    def attack(self, target):
        target._health -= self._attack

    def add_experience(self):
        self._experience = self._experience + 25
        if self._experience >= 0 and self._experience <= 99:
            self._lvl = 1
        elif self._experience >= 100 and self._experience <= 199:
            self._lvl = 2
        elif self._experience >= 200 and self._experience < 299:
            self._lvl = 3
        elif self._experience >= 300 and self._experience <= 399:
            self._lvl = 4
        elif self._experience >= 400 and self._experience <= 500:
            self._lvl = 5