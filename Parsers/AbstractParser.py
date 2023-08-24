import requests
from bs4 import BeautifulSoup


class AbstractParser:
    def __init__(self):
        self.web_site = 'this is web site'
        self.find_class = 'this is web site'

    def get_price_by_id(self, product_id):
        web_site_text = requests.get(self.web_site + product_id).text
        soup = BeautifulSoup(web_site_text, 'html.parser')
        return soup.find(class_=self.find_class).text
