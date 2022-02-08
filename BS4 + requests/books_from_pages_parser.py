from bs4 import BeautifulSoup as bs
# Модуаль по сбору книг со страницы

def get_books(pages):
    # Скармливаем html-код супу
    soup = bs(pages, 'html.parser')
    # Далее капаемся в тегах на странице и ищем нужные атрибуты
    # Метод select вытащит все теги указанные внутри выбранного тега(section)
    section = soup.select('section')[0]
    # Внутри тега section ищем блок с нужным контентом, в нашем случае - книги, ищем подходящий тег на странице
    books_block = section.select_one('ol[class=row]')
    # Углубляемся внутрь html страницы и внутри блока с книгами ищем сами книги
    # books является спиком, поэтому можем по нему пройтись в цикле, вытягивая нужные теги и элементы через find
    books = books_block.select('li')
    books_data = []
    for book in books:
        # Внутри блоков с книгами ищем нужный тег в котором находится картинка(div), внутри div ищем саму картинку
        image = 'https://books.toscrape.com/' + book.find('div', attrs={'class': 'image_container'}).find('img')['src']
        # Если есть атрибуты, вытаскиваем по ним(title)
        title = book.find('h3').find('a')['title']
        # Если нет атрибутов, вытаскиваем через функцию text
        price = book.find('p', attrs={'class': 'price_color'}).text
        book_dict = {'image': image,
                     'title': title,
                     'price': price}
        books_data.append(book_dict)
    return books_data
