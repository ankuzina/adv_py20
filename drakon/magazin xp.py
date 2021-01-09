#��� ������� ������
# ���������� money = 0
class Hero(Attacker):
    _health=100
    _attack=50
    _experience=0
    _money=0 # ���!!!!!!!!!
    def __init__(self,name):
        self._name=name
    def attack(self,target):
        target._health-=self._attack

#��� ��������
def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('�����', dragon._color, '������!')
        while dragon.is_alive() and hero.is_alive():
            print('������:', dragon.question())
            answer = annoying_input_int('�����:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('�����! \n** ������ ������ �� ���� **')
            else:
                dragon.attack(hero)
                print('������! \n** ��� ������ ����... **')
        if dragon.is_alive():
            break
        print('������', dragon._color, '��������!\n')
        hero._experience+=10
        hero._money+=(100*level) #��� �� ��� � ��������

    if hero.is_alive():
        print('�����������! �� ��������!')
        print('��� ����������� ����:', hero._experience)
        print('���� ����������� ���������:', hero._money)
    else:
        print('� ���������, �� ���������...')

def game_trollnament(hero, troll_list):
    for troll in troll_list:
        print('�����', troll._color, '������!')
        while troll.is_alive() and hero.is_alive():
            print('������:', troll.question())
            answer = input('�����:')

            if troll.check_answer(answer):
                hero.attack(troll)
                print('�����! \n** ������ ��������� **')
            else:
                troll.attack(hero)
                print('������! \n** �� ��� �������� �������... **')
        if troll.is_alive():
            break
        print('������', troll._color, '���������!\n')
        hero._experience+=20
        hero._money+=(200*level) #���

    if hero.is_alive():
        print('�����������! �� ��������!')
        print('��� ����������� ����:', hero._experience)
        print('���� ����������� ���������:', hero._money)
    else:
        print('� ���������, ��� �������...')

#������ ���� �������� �����
#� ������ ����� �������� ������������ ����� health � attack �� experience. �� �������� ����� ���:
# health. ����� ������ 50, 100, 200, 500 ������. ���������
print('��� �������� �����? ������� "health", "attack" ��� "exit"') #exit ��� ����� �����, ����� ��������� �� ������
health_price = {50: 10, 100: 20, 200: 40, 500: 100}
attack_price = {10: 5, 20: 10, 50: 25, 100: 200}
#h_price_new = ...
pokupka = input()
if pokupka == 'health':
    print('�� ������ ���������� 50 (�� 10), 100 (20), 200 (40), 500 (�� 100)')
    print('��������! ���� �� ��������� �������������� ������� �� ���� ������. ���� �� Healer, �� ���� ������� �� 2. ���� Jagernaut - ���������� �� 1,15, Wizard - �� 1,5, Imba - �� 5.')
    print('����� ����:')
    print('������ � ��� ', hero._experience, '����� �����')
    print('��� ����?')

    purchase = int(input())
    if purchase in health_price:
        if (hero._experience - hero._importance*health_price[purchase]) >= 0:
            hero._health += purchase
            hero._experience -= hero._importance*health_price[purchase]
            print('������ � ��� ', hero._health, '�������� � ', hero._experience, "�����")
        else:
            print("�� ��������")
            #�����
elif pokupka == 'attack':
    print('�� ������ ���������� 10 (�� 5), 20 (10), 50 (25), 100 (�� 200)')
    print('������ � ��� ', hero._attack, '����� ������')
    print('��� ����?')
    purchase = int(input())
    if purchase in attack_price:
        if (hero._experience - hero._importance*attack_price[purchase]) >= 0:
            hero._attack += purchase
            hero._experience -= hero._importance*attack_price[purchase]
            print('������ � ��� ', hero._attack, '������ � ', hero._experience, "�����")
        else:
            print("�� ��������")
            # �����
    #�������� ����������
elif pokupka == 'exit':
    print('��������!')
    #� ���-�� ���� ��������
else:
    print('�������')