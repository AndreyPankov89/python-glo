from bs4 import BeautifulSoup
import requests
import time

def parse(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
    
    values = soup.findAll('div', attrs={'itemprop':'review'})
    
    for value in values:
        autor_tag = value.find('meta', attrs={'itemprop':'author'})
        print(autor_tag['content'])
        
        reviewRating_tag = value.find('div', attrs={'itemprop':'reviewRating'})
        print(reviewRating_tag.meta['content'])     
       
        description_tag = value.find('meta', attrs={'itemprop':'description'})
        print(description_tag['content'])    
        
        datePublished_tag = value.find('meta', attrs={'itemprop':'datePublished'})
        print(datePublished_tag['content'] )      


headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'm.market.yandex.ru',
    'Sec-Fetch-Dest': 'ocument',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',    
    
}

url = 'https://market.yandex.ru/product--smartfon-apple-iphone-12-128gb/722974019/reviews?cpa=0&track=tabs'

response = requests.get(url, headers = headers)
response.encoding = 'utf-8'
data = response.text
parse(data)