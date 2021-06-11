import random

english = 'abcdefghjklmnopqrstuvwxyz'
russian ='абвгдежзийклмнопрстуфхцчшщъыьэюя'
digits = '0123456789'
sumbols = '!@#$%^&*_+='

characters = [english, english.upper(), russian, russian.upper(), digits, sumbols]

def is_valid(input_string):
    global top
    if (input_string.isdigit()):
        input_number = int(input_string)
        if (input_number > 0):
            return True
    return False

def is_options_valid (options):
    for key in options.split(' '):
        if not key.isdigit():
            return False
        if not int(key) in range(1, 7):
            return False
    return True


def generate_password(length, symbols):
    password = ''
    for i in range(0, length):
        number_of_symbol = random.randint(0, len(symbols)-1)
        password += symbols[number_of_symbol]
    return password

print('\n{:-^50}\n\n'.format('Вас приветствует генератор паролей'))


while True:
    while True:
        raw_number_of_passwords = input('Введите количество паролей: ')
        if (is_valid(raw_number_of_passwords)):
            break
        print('Не верный ввод, попробуйте снова. Требуется целое число')   
    number_of_passwords = int(raw_number_of_passwords)

    while True:
        raw_length_of_password = input('Введите требуемую длину пароля: ')
        if (is_valid(raw_length_of_password)):
            break
        print('Не верный ввод, попробуйте снова. Требуется целое число')
    length_of_password = int(raw_length_of_password)

    print('Опции пароля')
    print('1- строчные латинские буквы')
    print('2- заглавные латинские буквы')
    print('3- строчные русские буквы')
    print('4- заглавные русские буквы')
    print('5- цифры')
    print('6- спецсимволы')

    while True:
        raw_options = input('Введите номера необходимых опций через пробел: ')
        
        if (is_options_valid(raw_options)):
            break
        
        print('Ошибка ввода')
    options = [int(item) for item in raw_options.split(' ')]

    valid_chars = ''
    for key in options:
        valid_chars += characters[key-1]

    for i in range(0, number_of_passwords):
        print(generate_password(length_of_password, valid_chars))
    
    continue_generate = input('\nВы хотите сгенерировать еще пароли? (y/n) ')
    if (continue_generate.lower() == 'y'):
        continue
    else:
        print('\nСпасибо что воспользовались программой. Всего доброго')
        break
