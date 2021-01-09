# -*- coding: utf-8 -*-

#теперь надо написать магаз
#в магазе можно покупать определенное колво health и attack за experience. ну допустим будет так:
# health. можно купить 50, 100, 200, 500 единиц. стоимость
print('Что покупать будем? Введите "health", "attack" или "exit"') #exit это чтобы выйти, вдруг кириллицу не читает
health_price = {50: 10, 100: 20, 200: 40, 500: 100}
attack_price = {10: 5, 20: 10, 50: 25, 100: 200}
#h_price_new = ...
pokupka = input()
if pokupka == 'health':
    print('Вы можете приобрести 50 (за 10), 100 (20), 200 (40), 500 (за 100)')
    print('Внимание! Цены на улучшение характеристики зависят от вида игрока. Есть вы Healer, то цены делятся на 2. Если Jagernaut - умножаются на 1,15, Wizard - на 1,5, Imba - на 5.')
    print('Новые цены:')
    print('Сейчас у вас ', hero._experience, 'очков опыта')
    print('Что берём?')

    purchase = int(input())
    if purchase in health_price:
        if (hero._experience - hero._importance*health_price[purchase]) >= 0:
            hero._health += purchase
            hero._experience -= hero._importance*health_price[purchase]
            print('Теперь у вас ', hero._health, 'здоровья и ', hero._experience, "опыта")
        else:
            print("вы нищеброд")
            #выход
elif pokupka == 'attack':
    print('Вы можете приобрести 10 (за 5), 20 (10), 50 (25), 100 (за 200)')
    print('Сейчас у вас ', hero._attack, 'очков аттаки')
    print('Что берём?')
    purchase = int(input())
    if purchase in attack_price:
        if (hero._experience - hero._importance*attack_price[purchase]) >= 0:
            hero._attack += purchase
            hero._experience -= hero._importance*attack_price[purchase]
            print('Теперь у вас ', hero._attack, 'аттаки и ', hero._experience, "опыта")
        else:
            print("вы нищеброд")
            # выход
    #работает аналогично
elif pokupka == 'exit':
    print('Прощайте!')
    #и как-то надо вырулить
else:
    print('непонел')