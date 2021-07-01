russian_begin = 1040
russian_last = 1103
print('Введите букву:')
user_char = input()

if russian_last < ord(user_char) < russian_begin:
    print('Введите русскую букву')

print(chr(russian_begin), chr(russian_last))