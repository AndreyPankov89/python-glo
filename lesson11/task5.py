
numbers = input('Введите числа через пробел: ').split(' ')

for number in numbers:
    if (numbers.count(number)==1):
        print(number, end=' ') 