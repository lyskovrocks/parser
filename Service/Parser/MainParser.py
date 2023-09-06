import requests
from bs4 import BeautifulSoup

class MainParser:
    def __init__(self):
        self.web_site = 'this is a web site'
        self.find_class = 'this is a tag'

    def get_price_by_item(self, product_id):
        web_site_text = requests.get(self.web_site + product_id).text
        soup = BeautifulSoup(web_site_text, 'html.parser')
        price_today = soup.find_all(class_ = self.find_class)
        return price_today

    def __str__(self):
        return "abstract"






