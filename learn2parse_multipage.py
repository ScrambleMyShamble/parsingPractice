import requests
from bs4 import BeautifulSoup as bs
from learn2parse import get_books


def get_next_page(content):
    soup = bs(content, 'html.parser')
    try:
        # Следующая страница, ищем тег перехода на след.страницу
        next_page = 'https://books.toscrape.com/catalogue/' + soup.find('li', attrs={'class': 'next'}).find('a')['href']
        return next_page
    except:
        pass


