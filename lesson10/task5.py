start = ord(input('Введите первый символ '))
end = ord(input('Введите второй символ '))

if (start > end ):
    temp = end
    end = start
    start = temp

for char in range(start,end+1):
    print(chr(char))
    