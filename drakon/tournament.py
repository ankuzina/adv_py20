# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from random import randint


def palatka(_lvl):
    print('Представьтесь!')
    hero = Hero(input())
    print('Добро пожаловать в палатку!')
    print(
        'Что покупать будем? Введите "health", "attack" или "exit"')  # exit это чтобы выйти, вдруг кириллицу не читает
    health_price = {50: 10, 100: 20, 200: 40, 500: 100}
    attack_price = {10: 5, 20: 10, 50: 25, 100: 200}
    # h_price_new = ...
    pokupka = input()
    if pokupka == 'health':
        print('Вы можете приобрести 50 (за 10), 100 (20), 200 (40), 500 (за 100)')
        print(
            'Внимание! Цены на улучшение характеристики зависят от вида игрока. Есть вы Healer, то цены делятся на 2. Если Jagernaut - умножаются на 1,15, Wizard - на 1,5, Imba - на 5.')
        print('Новые цены:')
        print('Сейчас у вас ', hero._experience, 'очков опыта')
        print('Что берём?')

        purchase = int(input())
        if purchase in health_price:
            if (hero._experience - hero._importance * health_price[purchase]) >= 0:
                hero._health += purchase
                hero._experience -= hero._importance * health_price[purchase]
                print('Теперь у вас ', hero._health, 'здоровья и ', hero._experience, "опыта")
            else:
                print("вы нищеброд. сори. прощайте!")
                # выход
    elif pokupka == 'attack':
        print('Вы можете приобрести 10 (за 5), 20 (10), 50 (25), 100 (за 200)')
        print('Сейчас у вас ', hero._attack, 'очков аттаки')
        print('Что берём?')
        purchase = int(input())
        if purchase in attack_price:
            if (hero._experience - hero._importance * attack_price[purchase]) >= 0:
                hero._attack += purchase
                hero._experience -= hero._importance * attack_price[purchase]
                print('Теперь у вас ', hero._attack, 'аттаки и ', hero._experience, "опыта")
            else:
                print("вы нищеброд. копите опыт. пока.")
    elif pokupka == 'exit':
        print('Прощайте!')
    else:
        print('непонел')


def annoying_input_int(message=''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    if hero._lvl <= 1:
        for dragon in dragon_list:
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = annoying_input_int('Ответ:')

                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                break
            print('Дракон', dragon._color, 'повержен!\n')
        last_level = hero._lvl
        hero.add_experience()
    elif hero._lvl >= 2 and hero._lvl <= 4:
        for dragon in dragon_list:
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = annoying_input_int('Ответ:')
                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                break
            print('Дракон', dragon._color, 'повержен!\n')
        last_level = hero._lvl
        hero.add_experience()

    elif hero._lvl == 5:
        for dragon in dragon_list:
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = annoying_input_int('Ответ:')

                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                break
            print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        print('Ваш текущий уровень:', hero._lvl)
        print('Осталось опыта до следующего уровня:', hero._lvl * 100 - hero._experience)
        if last_level < (hero._lvl):
            palatka(last_level)
    else:
        print('К сожалению, Вы проиграли...')


def game_trollnament(hero, troll_list):
    for troll in troll_list:
        print('Вышел', troll._color, 'тролль!')
        while troll.is_alive() and hero.is_alive():
            print('Вопрос:', troll.question())
            answer = input('Ответ:')

            if troll.check_answer(answer):
                hero.attack(troll)
                print('Верно! \n** троллю неприятно **')
            else:
                troll.attack(hero)
                print('Ошибка! \n** от вас откусили кусочек... **')
        if troll.is_alive():
            break
        print('Тролль', troll._color, 'затроллен!\n')
    last_level = hero._lvl
    hero.add_experience()

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Прогресс в опыте:', hero._experience)
        print('Ваш текущий уровень:', hero._lvl)
        print('Осталось опыта до следующего уровня:', hero._lvl * 100 - hero._experience)
        if last_level < hero._lvl:
            palatka(last_level)
    else:
        print('К сожалению, Вас сожрали...')


def rod_dragon(number):
    if number % 100 in [11, 12, 13, 14]: return 'драконов'
    if number % 10 in [2, 3, 4]: return 'дракона'
    if number % 10 == 1:
        return 'дракон'
    else:
        return 'драконов'


def rod_troll(number):
    if number % 100 in [11, 12, 13, 14]: return 'троллей'
    if number % 10 in [2, 3, 4]: return 'тролля'
    if number % 10 == 1:
        return 'тролль'
    else:
        return 'троллей'


def start_game():
    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end='')
        hero = Hero(input())
        if hero._lvl == 1 or hero._lvl == 2:
            if randint(1, 2) == 1:
                dragon_number = randint(2, 3)
                dragon_list = generate_dragon_list(dragon_number)
                print('У Вас на пути', dragon_number, rod_dragon(dragon_number) + '!')
                game_tournament(hero, dragon_list)
            else:
                troll_number = randint(2, 3)
                troll_list = generate_troll_list(troll_number)
                print('Вам не дают пройти', troll_number, rod_troll(troll_number) + '!')
                game_trollnament(hero, troll_list)
        elif hero._lvl == 3 or hero._lvl == 4:
            if randint(1, 2) == 1:
                dragon_number = randint(2, 3)
                dragon_list = generate_mid_dragon_list(dragon_number)
                print('У Вас на пути', dragon_number, rod_dragon(dragon_number) + '!')
                game_tournament(hero, dragon_list)
            else:
                troll_number = randint(2, 3)
                troll_list = generate_mid_troll_list(troll_number)
                print('Вам не дают пройти', troll_number, rod_troll(troll_number) + '!')
                game_trollnament(hero, troll_list)
        elif hero._lvl == 5:
            if randint(1, 2) == 1:
                dragon_number = randint(1, 2)
                dragon_list = generate_hard_dragon_list(dragon_number)
                print('У Вас на пути', dragon_number, rod_dragon(dragon_number) + '!')
                game_tournament(hero, dragon_list)
            else:
                troll_number = randint(1, 2)
                troll_list = generate_hard_troll_list(troll_number)
                print('Вам не дают пройти', troll_number, rod_troll(troll_number) + '!')
                game_trollnament(hero, troll_list)
    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')