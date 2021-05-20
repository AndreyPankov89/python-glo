n = int(input('Введите количество элементов последовательности'))

tek_input =int(input('Введите очередное число последовательности'))
min = tek_input
max = tek_input
for i in range(1,n):
    tek_input =int(input('Введите очередное число последовательности'))
    if tek_input < min:
        min = tek_input
    if tek_input > max:
        max = tek_input

print('Минимум равен', min)
print('Максимум равен', max)