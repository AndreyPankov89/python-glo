sector = int(input('Введите номер сектора '))


if (sector == 0):
    print('Зеленый')
elif (sector>=1 and sector<=10 or sector>=19 and sector<=28):
    if (sector % 2 == 0):
        print('Черный')
    else:
        print('Красный')
elif (sector>=11 and sector<=18 or sector>=29 and sector<=36):
    if (sector % 2 == 0):
        print('Красный')
    else:
        print('Черный')
else:
    print('Ошибка ввода')