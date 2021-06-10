    
print('\n{:-^50}\n{:-^50}\n\n'.format('Добро пожаловать в игру','Задумайте число от 1 до 100'))


start = 1
end = 100
while True:
    guess = (start + end) // 2
        
    print('Если задуманное число больше {0}, введите 1'.format(guess))
    print('Если задуманное число меньше {0}, введите 2'.format(guess))
    print('Если задуманное число равно {0}, введите 0'.format(guess))

    user_answer = input()

    if (user_answer == '1'):
        start = guess
    elif (user_answer == '2'):
        end = guess
    else:
        print('УРА!!! ')
        break
    print()
