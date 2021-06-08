def count_digit(number):
    counter = 0
    while (number > 0):
        counter += 1
        number //= 10
    return counter

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

print(count_digit(first_number) * count_digit(second_number))