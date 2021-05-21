number = int(input('Введите целое число: '))

counter = 0

while (number % 2 == 0):
    counter += 1
    number = number // 2

print(counter)