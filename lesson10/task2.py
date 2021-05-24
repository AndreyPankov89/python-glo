chr_0 = ord('0')
chr_9 = ord('9')

character = ord(input('Введите символ: '))

if (character >= chr_0 and character <= chr_9):
    print('YES')
else:
    print('NO')