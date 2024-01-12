from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quotes import QuoteParser

class QuotesPage:
    def __init__(self,browser):
        self.browser = browser
        
    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.browser.fin_elements_by_css_selector(
            QuotesPageLocators.QUOTES
            )
        ]
        
    @property
    def author_drropdown(self) -> Select:
        element = self.browser.find_element_by_selector(
            QuotesPageLocators.AUTHOR_DROPDOWN
        )
        return Select(element)
    
    def select_author(self,author_name: str):
        self.author_drropdown.select_by_visible_text(author_name)
        
    
    
    