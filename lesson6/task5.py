email = input('Введите адрес электронной почты: ')

if ('@' in email and '.' in email):
    print('Корректный')
else:
    print('Некорректный')