from bs4 import BeautifulSoup
file = open('intensiv/reviews.html', 'r', encoding='utf-8')
data = file.read()
file.close()

def parse(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
    values = soup.findAll('div', attrs={'itemprop':'review'})

    for value in values:
        author_tag = value.find('meta', attrs={'itemprop': 'author'})
        print(author_tag['content'])
        rating_tag = value.find('div', attrs={'itemprop': 'reviewRating'})
        print(rating_tag.meta['content'])
        date_tag = value.find('meta', attrs={'itemprop': 'datePublished'})
        print(date_tag['content'])
        description_tag = value.find('meta', attrs={'itemprop': 'description'})
        print(description_tag['content'])
        print()

        
#print(soup.head.name, soup.head.text)

#for tag in soup.recursiveChiildGenerator():
#    print(tag)
parse(data)

