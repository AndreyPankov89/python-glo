a = int(input('Введите первое число '))
b = int(input('Введите второе число '))

if a > b:
    temp = b
    b = a
    a = temp
for i in range(a, b+1):
    print(i)