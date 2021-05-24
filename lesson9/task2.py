
number = int(input('Введите число: '))
flag  = 0
for i in range(4, number // 2 + 1):
    if (number % i == 0):
        flag = 1
        break

if (flag != 1):
    print('Число {0} простое'.format(number)) 
else:
    print('Число {0} составное'.format(number))