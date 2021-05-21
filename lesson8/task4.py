number = int(input('Введите натуральное число: '))

min = 10
max = 0
while (number != 0):
    curr_digit = number % 10
    if(curr_digit > max):
        max = curr_digit
    if (curr_digit < min):
        min = curr_digit
    number //= 10

print('Максимальная цифра равна',  max)
print('Миниимальная цифра равна',  min)
