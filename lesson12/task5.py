def is_star_date(date):
    date_parts = [int(i) for i in date.split('.')]
    return (date_parts[0] * date_parts[1] == date_parts[2] % 100)
        
date = input('Введите дату в формате дд.мм.гггг: ')

print(is_star_date(date))