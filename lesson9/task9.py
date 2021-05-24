n = int(input('Введите число: '))

while (n > 10):
    temp_n = n
    n = 0
    while (temp_n > 0):
        n += temp_n % 10
        temp_n //= 10

print(n)