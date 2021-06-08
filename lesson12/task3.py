def get_days_count(month):
    has_31_days = [1, 3, 5, 7, 8, 10, 12]
    has_30_days = [4, 6, 9, 11]

    if (month in has_31_days):
        return 31
    elif (month in has_30_days):
        return 30
    else:
        return 28

month = int(input('Введите номер месяца: '))

print(get_days_count(month))