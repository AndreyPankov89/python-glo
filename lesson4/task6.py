#Вводится одно целое четырехзначное число. Выведите максимальную цифру числа.


number = int(input("Введите целое четырехзначное число "))

first_digit = number // 1000
second_digit = number % 1000 // 100
thrid_digit = number % 100 // 10
fourth_digit = number % 10

max_digit = max(first_digit,second_digit,thrid_digit,fourth_digit)

print('У числа {0} максимальная цифра равна {1}'.format(number,max_digit))