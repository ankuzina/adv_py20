# -*- coding: utf-8 -*-
hero_attack = 1000
hero_experience = 1000
hero_health = 1000
hero_importance = 5

print('Что покупать будем? Введите "health", "attack" или "exit"') #exit это чтобы выйти, вдруг кириллицу не читает
health_price = {50: 10, 100: 20, 200: 40, 500: 100}
attack_price = {10: 5, 20: 10, 50: 25, 100: 200}
pokupka = input()
if pokupka == 'health':
    print('Вы можете приобрести 50 (за 10), 100 (20), 200 (40), 500 (за 100)')
    print('Сейчас у вас ', hero_experience, 'очков опыта')
    print('Что берём?')
    purchase = int(input())
    if purchase in health_price:
        if (hero_experience - hero_importance*health_price[purchase]) >= 0:
            hero_health += purchase
            hero_experience -= hero_importance*health_price[purchase]
            print('Теперь у вас ', hero_health, 'здоровья и ', hero_experience, "опыта")
        else:
            print("вы нищеброд")
            exit()
elif pokupka == 'attack':
    print('Вы можете приобрести 10 (за 5), 20 (10), 50 (25), 100 (за 200)')
    print('Сейчас у вас ', hero_attack, 'очков аттаки')
    print('Что берём?')
    purchase = int(input())
    if purchase in attack_price:
        if (hero_experience - hero_importance*attack_price[purchase]) >= 0:
            hero_attack += purchase
            hero_experience -= hero_importance*attack_price[purchase]
            print('Теперь у вас ', hero_attack, 'аттаки и ', hero_experience, "опыта")
        else:
            print("вы нищеброд")
            # выход
    #работает аналогично
elif pokupka == 'exit':
    print('Прощайте!')
    #и как-то надо вырулить
else:
    print('непонел')