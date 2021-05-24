while True:
    n = int(input('Введите число: '))
    if (n < 10):
        continue
    elif (n > 100):
        break
    else:
        print(n)
