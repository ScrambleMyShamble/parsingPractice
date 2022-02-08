import requests

from pages_parser import get_next_page  # парсит все страницы с сайта
from books_from_pages_parser import get_books  # парсит все книги со страниц
# модуль по запуску функций
# Пишем логику запуска функций

result_data = []
page_number = 1
url = 'https://books.toscrape.com/catalogue/page-1.html'
html_page = requests.get(url)  # первая страница
if html_page.status_code == 200:
    while True:
        books = get_books(html_page.content)  # отдаём первую страницу стразу функции по сбору книг
        print(f'{page_number} страница')
        result_data += books  # добавляем в результат уже спарсенные книги со страницы
        # далее пробуем получить след. страницу, отдать её функции get_book и так до момента пока страниц не останется
        next_page = get_next_page(html_page.content)  # получаем следующую страницу
        if next_page:  # если получена след. страница
            page_number += 1
            html_page = requests.get(next_page)  # в переменную текущей страницы записываем след.страницу
            print(f'Парсим страницу {page_number}')
        else:  # если страниц не осталось, цикл прерываем
            break
print(f'Данные собраны, {page_number} страниц')
