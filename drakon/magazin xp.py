#как копятся деньги
# изначально money = 0
class Hero(Attacker):
    _health=100
    _attack=50
    _experience=0
    _money=0 # опа!!!!!!!!!
    def __init__(self,name):
        self._name=name
    def attack(self,target):
        target._health-=self._attack

#сам механизм
def game_tournament(hero, dragon_list):
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
        hero._experience+=10
        hero._money+=(100*level) #опа но что с уровнями

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        print('Ваши накопленные лавандосы:', hero._money)
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
        hero._experience+=20
        hero._money+=(200*level) #опа

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        print('Ваши накопленные лавандосы:', hero._money)
    else:
        print('К сожалению, Вас сожрали...')

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