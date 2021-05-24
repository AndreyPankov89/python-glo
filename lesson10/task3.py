char_start = ord('А')
char_end = ord('Я')

character = ord(input('Введите символ: '))

if (character >= char_start and character <= char_end):
    print('YES')
else:
    print('NO')