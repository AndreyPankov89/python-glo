n = int(input('Введите число: '))
count_five = 0
for i in range(n+1):
    count_five += str(i).count('5')
print(count_five)