#Дано натуральное число, не превосходящее 1 000 000 000. Найдите сумму последних трех цифр. Последние цифры- это те, которые справа в числе.


number = int(input("Введите целое число "))
first_digit = number % 1000 // 100 
second_digit = number % 100 // 10
thrid_digit = number % 10

print('У числа {0} сумма последних трех цифр равна {1}'.format(number, first_digit + second_digit + thrid_digit))