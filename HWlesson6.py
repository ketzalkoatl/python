#easy
# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# скорость, цвет, имя, is_police - Булево значение.
# А так же несколько методов: go, stop, turn (direction) - которые должны сообщать,
# о том что машина поехала, остановилась, повернула (куда)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:
    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = False


    def go (self):
        print('машина {} поехала'.format(self.name))

    def stop(self):
        print('машина {} остановилась'.format(self.name))

    def turn_left(self):
        print('машина {} повернула на лево'.format(self.name))

    def turn_right(self):
        print('машина {} повернула на право'.format(self.name))

    def show (self):
        if self.is_police == False:
            print ('Название машины {}'.format(self.name),'\n', 'скорость  {} км/ч'.format(self.speed),'\n','цвет машины {}'.format(self.colour),'\n', 'машина не является полицейской' )
        if self.is_police == True:
            print('Название машины {}'.format(self.name), '\n','скорость  {} км/ч'.format(self.speed), '\n', 'цвет машины {} '.format(self.colour), '\n', 'машина является полицейской')


class SportCar (TownCar):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)


class WorkCar (TownCar):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)

class PoliceCar(TownCar):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)
        self.is_police = True

    def beep(self):
        print('полицейская машина включила мигалку')

                    # normal
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random
class Person():
    def __init__(self, name, strength, agility, intelligence):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.health = 500
        self.damage = 10*strength
        self.magickadamage = 10*intelligence
        self.armor = 1+strength*0.1
        self.magickarmor = 1+intelligence*0.1
    def _use_attack(self, taking_damage):
        taking_damage.health -= self.damage/taking_damage.armor

    def dodge(self):
        dodge_chance = random.randrange(0 - self.agility*2, 100 -self.agility*5)
        return dodge_chance

    def use_magic(self, taking_damage):
        print('магическая атака пытается влететь в лицо противника')
        taking_damage.health -= self.magickadamage / taking_damage.magickarmor


class Combat_scheme():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        while True:
            dodge_chance= player.dodge()
            if dodge_chance <= 15:
                print ('Ваша изворотливость потрясает')
            if dodge_chance > 15:
                enemy._use_attack(player)
                print('Вы не смогли уйти от удара. у вас осталось {} жизней'.format(player.health))
            if player.health <= 0:
                print('{} выйграл, у него осталось {} жизней'.format(enemy.name, enemy.health))
                break
            choice = int(input ('выберите способ атаки: \n 1 - физический урон, \n 2 - магический урон'))
            if choice == 1:
                a=enemy.dodge()
                if a <= 15:
                    print("враг увернулся")
                if a > 15:
                    player._use_attack(enemy)
                    print('у врага осталось {} жизни'.format(enemy.health))
            if choice == 2:
                print('магическая атака пытается влететь в лицо противника')
                a = enemy.dodge()
                if a <= 15:
                    print('магическая субстанция пролитает мимо врага со свисто')
                if a > 15:
                    player.use_magic(enemy)
            if enemy.health <=0:
                print('{} выйграл, у него осталось {} жизней'.format(player.name, player.health))
                break






class Player(Person):
    def __init__(self, name, strength, agility, intelligence):
        super().__init__(name, strength, agility, intelligence)
# ______________________________________________________________________________________________________
enemy_list = [['john', 5, 10, 5],['Alisia', 10, 5, 5], ['Nick', 10, 7, 8], ['Vasiliy', 7, 10, 5], ['cheater', 10, 10, 10]] #список вргов
enemy = enemy_list[random.randrange(0,5)]   # выбор врага
enemy_name = enemy[0]                       #имя
enemy_strength = enemy[1]                   #сила
enemy_agility = enemy[2]                    #ловкость
enemy_intelligence = enemy[3]               #интелект
evil_enemy = Person(enemy_name, enemy_strength, enemy_agility, enemy_intelligence)    # передаю статы для создания персонажа класса
while True:                                 #цикл для создания персонажа не в идеале очки не должны привышать 22
    print(' вы можете ввести характеристи сила, ловкость и интелект.\n в сумме они не должны привышать 22 очка')
    name = input('Введите имя персонажа')
    strength = int(input('укажите силу вашего персонажа'))
    agility = int(input('укажите ловкость вашего персонажа'))
    intelligence = int(input('укажите интелект вашего персонажа'))
    count = strength + agility + intelligence   # счетчик суммы очков
    if  count <=22:
        break
player=Player( name, strength, agility, intelligence)   # создание класса игрока
print('{} с парамиетрами:\n сила - {}\n ловкость - {}\n интелект - {}\n сражается против\n {} с парамиетрами:\n сила - {}\n ловкость - {}\n интелект - {}'.format(player.name, player.strength, player.agility, player.intelligence, evil_enemy.name, evil_enemy.strength, evil_enemy.agility, evil_enemy.intelligence))
start_game = Combat_scheme(player, evil_enemy)       # начало игры
                            # hard
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка







 #__________________________необходимо добавить учет ошибок а так же выход и надо было оформить некоторые шаги как функции
standard_toy_list = [['простой предприятия', 'цвет унылости', 0, 0, 0, ],['Самолетик', 'синий', 10000, 300, 90000, ],['Пистолет', 'черный', 15000, 300, 99000, ], ['Кукла', 'разноцветная', 16000, 300, 100000, ]]
animal_toy_list= [['простой предприятия', 'цвет унылости', 0, 0, 0, ],['Лев', 'фиолетовый', 20000, 500, 300000, ],['Медведь', 'серый', 35000, 400, 190000, ], ['Жираф', 'разноцветный', 160000, 400, 500000, ]]
cartoon_characters_list= [['простой предприятия', 'цвет унылости', 0, 0, 0, ],['Мики-Маус', 'разноцветный', 200000, 500, 900000, ],['Гомер Симпсон', 'разноцветный', 200000, 400, 700000, ], ['Чебурашка', 'разноцветный', 400000, 600, 1000000, ]]


class Standard_Toy():                         #стандартная игрушка
    def __init__(self, name, сolour, price_of_material, hours_of_work, selling_price):
        self.name = name
        self.color = сolour
        self.price_of_material = price_of_material
        self.hours_of_work = hours_of_work
        self.selling_price = selling_price


class Animals(Standard_Toy):
    def __init__(self, name, сolour, price_of_material, hours_of_work, selling_price):
        super().__init__(name, сolour, price_of_material, hours_of_work, selling_price)




class Cartoon_characters(Standard_Toy):
    def __init__(self, name, сolour, price_of_material, hours_of_work, selling_price):
        super().__init__(name, сolour, price_of_material, hours_of_work, selling_price)




class Factory:
    def __init__(self, name, balance):
        self.name = name                        #   имя фабрики игрушек
        self.balance = balance                  #   баланс фирмы идет на закупку ресурсов и оплату человекочасов
        self.storage = []                       #   склад
        self.salary = 200                       #   зарплата за один час работы

    def making_basis(self, type_of_toy):
        salary = type_of_toy.hours_of_work/3*self.salary
        self.balance -= type_of_toy.price_of_material - salary
        print('Фабрика игрушек {} создала базу для паритии игрушек {}. Вы заплатили зарплату рабочим в размере {} '.format(self.name, type_of_toy.name, salary))
    def stitching (self, type_of_toy):
        salary = type_of_toy.hours_of_work / 3 * self.salary
        self.balance -= salary
        print('Фабрика игрушек {} пошила основу паритии игрушек {}. Вы заплатили зарплату рабочим в размере {} '.format(self.name, type_of_toy.name, salary))
    def painting(self,type_of_toy):
        salary = type_of_toy.hours_of_work / 3 * self.salary
        self.balance -= salary
        self.storage.append(type_of_toy.selling_price)
        print(' вы создали партию игрушки {}, перемещаем ее на склад. Так же вы заплатили зарплату работникам в размере {} и потратили денег на материалы в размере {}'.format(type_of_toy.name, salary, type_of_toy.price_of_material))
        factory.menu()
    def sell_all (self):
        self.balance+=sum(self.storage)
        self.storage.clear()
        print('вы продали все со склада, машины с игрушками уже в пути, а вам на баланс пришла сумма в размере {}. Ваш баланс составляет {}'.format(sum(self.storage), self.balance))
        factory.menu()
    def menu (self):
        solution = int(input(' выберите действие \n'
                              '1 - создание игрушки '
                              '2 - продажа со склада'
                              '3 - показ баланса'))
        if solution== 1:
            choice = int(input('выберете тип игрушки который хотите создавать\n'
            '{} - 1\n'
            '{} - 2\n'
            '{} - 3\n'.format('стандартные игрушки', 'животные', 'персонажи мультфильмов')))
            if choice == 1:
                print('вы можете создать :\n', standard_toy_list[1][0], standard_toy_list[2][0],
                      standard_toy_list[3][0])
                choice = int(input('выберете что собираетесь создавать\n'
                                   '{} - 1\n'
                                   '{} - 2\n'
                                   '{} - 3\n'.format(standard_toy_list[1][0], standard_toy_list[2][0],
                                                     standard_toy_list[3][0])))
                name = standard_toy_list[choice][0]
                сolour = standard_toy_list[choice][1]
                price_of_material = standard_toy_list[choice][2]
                hours_of_work = standard_toy_list[choice][3]
                selling_price = standard_toy_list[choice][4]
                toy = Standard_Toy(name, сolour, price_of_material, hours_of_work, selling_price)
            if choice == 2:
                print('вы можете создать :\n', animal_toy_list[1][0], animal_toy_list[2][0], animal_toy_list[3][0])
                choice = int(input('выберете что собираетесь создавать\n'
                                   '{} - 1\n'
                                   '{} - 2\n'
                                   '{} - 3\n'.format(animal_toy_list[1][0], animal_toy_list[2][0],
                                                     animal_toy_list[3][0])))
                name = animal_toy_list[choice][0]
                сolour = animal_toy_list[choice][1]
                price_of_material = animal_toy_list[choice][2]
                hours_of_work = animal_toy_list[choice][3]
                selling_price = animal_toy_list[choice][4]
                toy = Animals(name, сolour, price_of_material, hours_of_work, selling_price)
            if choice == 3:
                print('вы можете создать :\n', cartoon_characters_list[1][0], cartoon_characters_list[2][0],
                      cartoon_characters_list[3][0])
                choice = int(input('выберете что собираетесь создавать\n'
                                   '{} - 1\n'
                                   '{} - 2\n'
                                   '{} - 3\n'.format(cartoon_characters_list[1][0], cartoon_characters_list[2][0],
                                                     cartoon_characters_list[3][0])))
                name = cartoon_characters_list[choice][0]
                сolour = cartoon_characters_list[choice][1]
                price_of_material = cartoon_characters_list[choice][2]
                hours_of_work = cartoon_characters_list[choice][3]
                selling_price = cartoon_characters_list[choice][4]
                toy = Cartoon_characters(name, сolour, price_of_material, hours_of_work, selling_price)
            factory.making_basis(toy)
            factory.stitching(toy)
            factory.painting(toy)
        if solution == 2:
            factory.sell_all()
        if solution == 3:
            print(self.balance)
easy = 1
normal = 2
hard = 3
name = input(' введите название вашей фабрики\n')
choose_you_destiny = int(input('выберете сложность игры\n'
                           'Easy - 1\n'
                           'Normal - 2\n'
                           'Hard - 3\n'))
if choose_you_destiny==easy:
    balance = 2000000
if choose_you_destiny==normal:
    balance = 1520000
if choose_you_destiny==hard:
    balance = 1000000
factory = Factory(name, balance)
print( ' фабрика игрушек с названием {}, имеет счет (баланс) размером - {} '.format(factory.name, factory.balance))
factory.menu()