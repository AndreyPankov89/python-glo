n = int(input('Введите количество чисел: '))

hasOdd  = 'NO'
for i in range(0,n):
    current_number = int((input('Введите очередное число: ')))
    if (current_number % 2 == 1):
        hasOdd = 'YES'

print(hasOdd)