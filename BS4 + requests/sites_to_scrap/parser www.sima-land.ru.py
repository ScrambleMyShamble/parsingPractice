import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.sima-land.ru/promo/rasprodazha-avtotovarov-2022/?c_id=700705051&per-page=20&sort=price&viewtype=list'
get_page = requests.get(url).content
soup = bs(get_page, 'html.parser')
basic_div = soup.findAll('div', {'class': 'ZjHGY'})[0]
result_list = []
for item in basic_div:
    title = item.findAll('span', {'class': '_3JJFA'})[0].get_text()
    price = item.findAll('span', {'class': 'ObDrR', 'data-testid': 'price'})[0].get_text().replace('\u2009', '')
    image = item.findAll('img', {'class': '_1EP0z'})[0]['src']
    item_dict = {'title': title,
                 'price': price,
                 'image': image}
    result_list.append(item_dict)
for it in result_list:
    print(it)
