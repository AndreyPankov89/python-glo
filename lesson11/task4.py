from math import ceil
numbers = input('Введите числа через пробел: ').split(' ')

count_paris = 0
for number in numbers:
    if (numbers.count(number)>1):
        count_paris += numbers.count(number) - 1
print(ceil(count_paris/2)) 