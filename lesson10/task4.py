chr_a = ord('a')
chr_z = ord('z')

character = ord(input('Введите символ'))

if (character >= chr_a and character <= chr_z):
    character = chr(character).upper()
else:
    character = chr(character)
print(character)