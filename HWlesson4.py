# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов списка


[1, 2, 4, 0] -> [1, 4, 16, 0]
my_list = [3, 7, 10, 13, 5, 12, 77]
my_list2 = [ i*i for i in my_list]
print(my_list2)



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruit_list1 = ["яблоко", "груша", "апельсин", "банан", "томат"]
fruit_list2 = ["груша", "апельсин", "банан", "манго", "яблоко"]
fruit_list3 = [ i for i in fruit_list2 if i==i in fruit_list1]
print(fruit_list3)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов объекта, удовлетворяющих следующие правила:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4й


list_with_int = [120, 1500, 34, 33, -24, 81, 0, -555, 231, 253, 256, 75, - 99, 3, 91, 12, 24, 83]
list_with_selected_choice = [number for number in list_with_int if number > 0 and number%3==0 and number%4==0]
print(list_with_selected_choice)



# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.



import re
name_surname_pattern = '[A-Z][a-z]+'#паттерн на имя и фамилию
mail_pattern = '[a-z_0-9]+@[a-z]+\.(ru|org|com)'#паттерн на почту
while True:
    name = input('введите имя')
    match= re.fullmatch(name_surname_pattern, name)
    if match:
        print('Имя принято')
        break
    else:
        print('Введите еще раз')

while True:
    surname = input('введите фамилию')
    match= re.fullmatch(name_surname_pattern, surname)
    if match:
        print('Фамилия принята')
        break
    else:
        print('Попытайтесь еще раз')

while True:
    mail = input('введите почту')
    match = re.fullmatch(mail_pattern, mail)
    if match:
        print('почта принята')
        break
    else:
        print('Попытайтесь еще раз')
print('Проверка пройдена')


# Задача - 2:
# Вам дан текст:
# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

import re
pattern = '\.+'
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''
match= re.search(pattern, some_str)
if match:
    print('в тексте присутствуют более одной точки подряд')
else:
    print('все чисто')


# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:         # вместо ==0 >=0
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:                         #убрал '' для аcсоциации int
        print(check_account(person))
    elif choice == 2:                       #убрал '' для аcсоциации int
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))


def start():
    while True:
        try:
            card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
        except ValueError:
            print('введите корректные данные')
        try:
            card_number = int(card_number)
        except UnboundLocalError:
            pass
        except ValueError:
            print('необходимо ввести данные в формате "0000000000000000 0000"')
        try:
            pin_code = int(pin_code)
        except ValueError:
            print('необходимо ввести данные в формате "0000000000000000 0000"')
        except UnboundLocalError:
            pass
        person = get_person_by_card(card_number)
        if person and is_pin_valid(person, pin_code):
            while True:
                choice = int(input('Выберите пункт:\n'
                                '1. Проверить баланс\n'
                                '2. Снять деньги\n'
                                '3. Выход\n'
                                '---------------------\n'
                                'Ваш выбор:'))
                if choice == 3:
                    break
                process_user_choice(choice, person)
        else:
            print('Номер карты или пин код введены не верно!')
start()