def find_max(list):
    max = int(list[0])
    for item in list:
        if (int(item) > max):
            max = int(item)

    return max

first_list = [int(i) for i in input('Введите элементы первого списка через пробел: ').split(' ')]
second_list = [int(i) for i in input('Введите элементы второго списка через пробел: ').split(' ')]

print(find_max(first_list) * find_max(second_list))