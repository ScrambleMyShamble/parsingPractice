import requests
import bs4
from bs4 import BeautifulSoup as bs

url = 'https://platffin.com/magazin/folder/tovary-so-skidkoj-do-70'
get_page = requests.get(url).content
soup = bs(get_page, 'html.parser')
basic_div = soup.findAll('div', {'class': 'product-list product-list-thumbs'})[0]
result = []
for item in basic_div:
    if type(item) == bs4.element.Tag:
        if len(item.findAll('div', {'class': 'product-name'})) > 0:
            title = item.findAll('div', {'class': 'product-name'})[0].get_text()
            price = item.findAll('div', {'class': 'price-current'})[0].get_text().replace('\n', '').replace('\t\t\t',
                                                                                                            '')
            image = 'https://platffin.com/' + item.findAll('a')[0].find('img')['src']
            source_dict = {'title': title,
                           'price': price,
                           'image': image}
            result.append(source_dict)
    else:
        continue

for item in result:
    print(item)
