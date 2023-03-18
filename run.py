# Import Packages
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-news-populer')
def detik_news_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler')

    bs = BeautifulSoup(html_doc.text, 'html.parser')

    populer_news = bs.find(attrs={'class': 'grid-row list-content'}) 

    titles = populer_news.findAll(attrs={'class': 'media__title'})
    images = populer_news.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=images)




if __name__ == '__main__':
    app.run(debug=True)