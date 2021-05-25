chr_a = ord('a')
chr_z = ord('z')
chr_A = ord('A')
chr_Z = ord('Z')

character = ord(input('Введите символ'))

if (character >= chr_a and character <= chr_z):
    character = chr(character).upper()
elif (character >= chr_A and character <= chr_Z):
    character = chr(character).lower()
else:
    character = chr(character)
print(character)