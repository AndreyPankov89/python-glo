number = int(input('Введите натуральное число: '))

counter = 0

while (number != 0):
    if (number % 10 == 5):
        counter += 1
    number //= 10

print(counter) 