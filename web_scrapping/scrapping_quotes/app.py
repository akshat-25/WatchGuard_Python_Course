from selenium import webdriver

from pages.quotes_page import QuotesPage

firefox = webdriver.Firefox()
firefox.get('https://quotes.toscrape.com/')
page = QuotesPage(firefox)


for quote in page.quotes:
    print(quote.content)
    

