import requests
import logging
import time

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y %H:%M:%S',
                    level = logging.DEBUG,
                    filename='logs1.txt')

logger = logging.getLogger('scraping')

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books

for page_num in range(1,page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = request.get(url).content
    logger.debug('Creating AllBooksPage logging.')
    page = AllBooksPage(page_content)
    books.extend(pages.books)
    