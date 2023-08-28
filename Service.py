import requests
from bs4 import BeautifulSoup


class MainParser:
    def __int__(self):
        self.web_site = 'this is a web site'
        self.find_tag = 'this is a tag'

    def get_price_by_item(self, product_id):
        web_site_text = requests.get(self.web_site + product_id).text
        soup = BeautifulSoup(web_site_text, 'html.parser')
        price_today = soup.find(self.find_tag).text
        return price_today


class Mirm(MainParser):
    def __int__(self):
        self.web_site = 'https://mirm.ru/catalog/products/'
        self.find_tag = "id='results-price'"


class PopMusic(MainParser):
    def __int__(self):
        self.web_site = 'https://pop-music.ru/products/'
        self.find_tag = "class_='productfull__newprice'"
