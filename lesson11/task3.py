address = input('Введите IP адрес: ')
result = 'YES'
for octet in address.split('.'):
    if (int(octet)>255):
        result = 'NO'
print(result)