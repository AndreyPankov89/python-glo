ticket_number = int(input('Введите номер билета '))

first_sum = (ticket_number // 100000) + (ticket_number % 100000 // 10000) + (ticket_number % 10000 // 1000) 
second_sum = (ticket_number % 1000 // 100) + (ticket_number % 100 // 10) + (ticket_number % 10) 

if (first_sum == second_sum):
    print("Билет {0} счастливый".format(ticket_number))
else:
    print("Билет {0} НЕсчастливый".format(ticket_number))