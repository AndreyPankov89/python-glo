number = int(input('Введите натуральное число: '))

temp_number = number #копия, для того чтобы резать, так как нужно сохранить исходное число
sum_of_digits = 0
while (temp_number != 0):
    sum_of_digits += temp_number % 10
    temp_number //= 10

if (number % sum_of_digits == 0):
    print('YES')
else:
    print('NO')
