import random
def generate_secret_word():
    symbols = ['1','2', '3','4', '5', '6', '7', '8', '9', '0']
    secret_word = ''
    for i in range(4):
        random_index = random.randint(0, len(symbols)-1)
        secret_word += symbols[random_index]
        symbols.pop(random_index)
    return secret_word

def count_bulls(user_word, secret_word):
    counter = 0
    for i in range(4):
        if (user_word[i] == secret_word[i]):
            counter +=1
    return counter


def count_cows(user_word, secret_word):
    counter = 0
    for i in range(4):
        if (user_word[i] != secret_word[i] and user_word[i] in secret_word):
            counter +=1
    return counter

def test_input(input):
    if (len(input)!=4):
        return False
    sett = set()
    for char in input:
        if (char.isdigit()):
            sett.add(char)

    return len(sett)==4

def play_game():
    secret_word = generate_secret_word()
    tru_count =0
    while True:

        while True:
            user_word = input('Введите 4 различных цифры: ')
            if (test_input(user_word)):
                break
            else:
                print('Некорректный ввод. Попробуйте снова')
        tru_count += 1
        cows = count_cows(user_word, secret_word)
        bulls = count_bulls(user_word, secret_word)

        if (bulls == 4):
            print('Вы выиграли за {0} попыток!'.format(tru_count))
            break
        else:
            print('{0} быков, {1} коров'.format(bulls, cows))

while True:
    play_game()
    continue_game = input('Начать новую игру? (y/n) ')
    if (continue_game.lower() == 'y'):
        continue
    else:
        break