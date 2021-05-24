number = int(input('Введите натуральное число: '))
flag = 'NO'
while (number != 0):
    if (number % 10 == 1):
        flag = "YES"
        break
    number //= 10

print(flag)