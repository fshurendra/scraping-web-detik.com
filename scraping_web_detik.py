import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler')

bs = BeautifulSoup(html_doc.text, 'html.parser')

populer_news = bs.find(attrs={'class': 'grid-row list-content'}) 

titles = populer_news.findAll(attrs={'class': 'media__title'})
images = populer_news.findAll(attrs={'class': 'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])

# print(populer_news)