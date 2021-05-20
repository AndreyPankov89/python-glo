n = int(input('Введите количество чисел: '))
all_odd  = 'YES'
for i in range(0,n):
    current_number = int((input('Введите очередное число: ')))
    if (current_number % 2 == 0):
        hasOdd = 'NO'

print(all_odd)