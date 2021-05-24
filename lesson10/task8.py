str = input('Введите строку: ')
counter = 0
for i in range(len(str)-1):
    if (str[i] == str[i+1]):
        counter += 1
print(counter)