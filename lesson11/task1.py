n = int(input('Введите количество фраз '))
phrases = []
for i in range(n):
    phrases.append(input())

search_phrase = input('Введите фразу для поиска ')

for phrase in phrases:
    if(search_phrase.lower() in phrase.lower()):
        print(phrase)