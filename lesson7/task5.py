n = int(input('Введите натуральное число от 1 до 9 '))

for i in range(1, 11):
    print('{0} x {1} = {2}'.format(n, i, n * i))