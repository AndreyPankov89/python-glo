n = int(input('Введите натуральное число: '))

for i in range(1, n+1):
    if ((i>=2 and i<=8) or (i>=128 and i<=256) or (i>=1024 and i<=2048)):
        continue
    else:
        print(i)
