from math import ceil
numbers = input('Введите числа через пробел: ').split(' ')

count_paris = 0
for number in numbers:
    if (numbers.count(number)==1):
        print(number, end=' ') 