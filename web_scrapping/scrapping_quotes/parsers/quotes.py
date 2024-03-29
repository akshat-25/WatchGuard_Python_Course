from locators.quote_locators import QuotesLocators

class QuoteParser:
    def __init__(self,parent):
        self.parent = parent
        
    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'
        
    @property
    def content(self):
        locator = QuotesLocators.CONTENT_LOCATOR
        return self.parent.find_element_by_selector(locator).text
    
    @property
    def author(self):
        locator = QuotesLocators.AUTHOR
        return self.parent.find_element_by_selector(locator).text
    
    @property
    def tags(self):
        locator = QuotesLocators.TAGS
        return self.parent.find_element_by_selector(locator)
    
    
    