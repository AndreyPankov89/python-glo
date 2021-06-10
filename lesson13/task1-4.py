import random

def is_valid(input_string):
    global top
    if (input_string.isdigit()):
        input_number = int(input_string)
        if (input_number > 0 or input_number <= top):
            return True
    return False

# вроде оптимальный вариант ищу банальным бинарным поиском, но иногда получается сыграть лучше оптимального
def guesser(start, end, secret):
    guess = (end + start) // 2
    if (guess > secret):
        return guesser(start, guess, secret) + 1
    elif(guess < secret):
        return guesser(guess,end,secret) + 1
    else:
        return 1
    
print('\n{:-^50}\n{:-^50}\n\n'.format('Добро пожаловать в игру','УГАДАЙ ЧИСЛО'))

top = int(input('Введите верхнюю границу: '))
secret_number = 0;


def init_game():
    global secret_number, counter_of_guess, optimal_guess
    secret_number = random.randint(1, top)
    counter_of_guess = 0
    optimal_guess = guesser(1,top,secret_number)

init_game()

while True:
    input_string = input('Введите число от 1 до ' + str(top))
    if (not is_valid(input_string)):
        continue

    user_number = int(input_string)
    counter_of_guess += 1
    if (user_number > secret_number):
        print('Загаданное число меньше введенного')
    elif (user_number < secret_number):
        print('Загаданное число больше введенного')
    else:
        print("Поздравляем! Вы угадали число за {0} попыток, оптимально {1} попыток. Хотите сыграть еще? (y/n): ".format(counter_of_guess, optimal_guess), end='')   
        continue_game = input()
        if (continue_game.lower() == 'y'):
            init_game()
        else:
            break

