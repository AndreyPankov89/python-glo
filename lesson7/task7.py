n = int(input('Введите натуральное число: '))
mul = 1
flag = 0
for i in range(1,n+1):
    last_digit = i % 10
    if (last_digit  == 2 or last_digit == 9):
        mul *= i
        flag = 1
print(mul*flag)