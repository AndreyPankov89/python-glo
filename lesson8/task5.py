positiv_counter = 0
negativ_counter = 0

number = int(input('Введите очередное число: '))

while (number != 0):
    if (number > 0):
        positiv_counter += 1
    if (number < 0):
        negativ_counter += 1    
    number = int(input('Введите очередное число: '))


print(positiv_counter * negativ_counter)