summator = 0
counter = 0

number = int(input('Введите очередное число: '))

while (number != 0):
    summator += number
    counter += 1    
    number = int(input('Введите очередное число: '))

if (counter != 0):
    print(summator /  counter)
else:
    print('Последовательность пуста')