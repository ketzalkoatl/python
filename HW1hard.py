while True:
    print("Для прохождения медицинской анкенты необходимо ввести ваши данные")
    name = input("Введите ваше имя  ")
    surname = input("Введите вашу фамилию  ")
    age = int(input("введите ваш возраст  "))
    weight = int(input("введите ващ вес "))
    b = "Эта информация верна?" "Вас зовут: " "\n" + surname + " " + name + "\n""ваш возраст и вес: " + str(age) + " лет  " + str(weight) + " кг"
    print (b)
    a = (input("напишите да или нет"))

    c = "да"
    if c == a:
        print("Хорошо,продолжим.")
        break
    else:
        print("введите корректные данные")
if age < 30 and weight >= 50 and  weight <= 120:
    print ( name + " " + surname +" Вы в хорошем состоянии")
if age > 30 and weight < 50 and weight > 120:
    print(name + " " + surname + " Вам надо былобы начать вести правильный образ жизни")
if age > 40 and weight < 50 and weight > 120:
    print(name + " " + surname + " Срочно необходим врачебный осмотр")
if age > 30 and weight >= 50 and  weight <= 120:
    print ( name + " " + surname +"Вы все еще в хорошем состоянии")
