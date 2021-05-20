n = int(input('Введите натуральное число: '))
sum = 0
for i in range(1,n+1):
    last_digit = i % 10
    if (last_digit  == 1 or last_digit == 3 or  last_digit == 7):
        sum += i

print(sum)