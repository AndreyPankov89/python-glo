"""
На вход программе вводится одно целое положительное число, меньшее 1000.
Выведите сумму и произведение цифр данного числа.
"""

number = int(input("Введите число, меньше 1000:"))
first_digit = number // 100 
second_digit = number % 100 // 10
thrid_digit = number % 10

print('Сумма цифр числа {0}  равна {1}'.format(number, first_digit + second_digit + thrid_digit))
print('Произведение цифр числа {0}  равно {1}'.format(number, first_digit * second_digit  * thrid_digit))

# В задании возможно стоит уточнить, что трехзначное число нужно, так как в противном случае, произведение всегда 0.
# Ну или решать через циклы или строки, что пока "не умеем"