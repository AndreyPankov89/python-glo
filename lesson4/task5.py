"""
Вводится одно целое число - количество секунд, который показывает секундомер на телефоне.

Вам стало интересно, сколько это будет часов, минут и секунд.
"""

time = int(input("Введите количество секунд: "))

hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60

print('{0} секунд - это {1} час {2} минут {3} сек'.format(time,hours,minutes,seconds))