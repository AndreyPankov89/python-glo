import random
questions = [
    ' Человеческие способности довольно велики. Например, мы можем собственными силами разогнать воздушный поток до 150–170 км/ч. В процессе чего человек способен произвести такой воздушный поток?', 
    'Польский ученый-математик Гуго Дионисий Штейнгауз, прославившийся также своими афоризмами, говорил: «Комплимент женщине должен быть правдивее, чем...»',
    'Что использовали в Китае для глажки белья вместо утюга?',
    ' В 1931 году Аркадий Райкин сам придумал и произнес со сцены некое слово. Оно стремительно вошло в обиход - так стали называть несуразную легкую сумку.',
    'В словаре Владимира Ивановича Даля встречается старинное название барометра. Какое?'
]

answers = [
    'чихание',
    'правда',
    'сковорода',
    'авоська',
    'буревесник'
]


def check_input(letter):
    char_start = ord('а')
    char_end = ord('я')
    character = ord(letter)
    if (character >= char_start and character <= char_end):
        return True
    else:
        return False

def check_repiat(character):
    if (character in input_symbols):
        return True
    else:
        return False

def init_game():
    global word, display_string, counter, input_symbols
    number = random.randint(1,5)
    print (questions[number])
    word = answers[number]
    display_string = '*' * len(word)
    counter = 0
    input_symbols = ''

init_game()

while True:
    print(display_string)
    input_letter = input('Введите букву ').lower()
    if (not check_input(input_letter)):
        print('Символ не является буквой русского алфавита')
        continue

    if (check_repiat(input_letter)):
        print('Символ был введен ранее')
        continue

    counter += 1
    input_symbols += input_letter
    if (input_letter in word):
        new_display_string = ''
        for i in range(len(word)):
            letter = word[i]
            if (letter == input_letter):
                new_display_string += input_letter
            else:
                new_display_string += display_string[i]
        display_string = new_display_string
        print('Есть такая буква')
    else:
        print('Нет такой буквы ')
    if (display_string == word):
        print("Поздравляем! Вы угадали слово за {0} попыток. Хотите сыграть еще? (y/n): ".format(counter), end='')   
        continue_game = input()
        if (continue_game.lower() == 'y'):
            init_game()
        else:
            break

