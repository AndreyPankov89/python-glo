def get_delivery_price(items_count):
    return items_count * 50 + 50

items_count = int(input('Введите количество доставляемых товаров: '))

print(get_delivery_price(items_count))