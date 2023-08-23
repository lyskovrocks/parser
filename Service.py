import requests
from bs4 import BeautifulSoup

class Music_price:
    def get_price(self, product_name):
        find_product = product_name
        web_site_text = requests.get(self.web_site + find_product).text
        soup = BeautifulSoup(web_site_text, 'html.parser')
        price_today = soup.find(class_='productfull__newprice').text
        # price_today_int = int(price_today[0:-2].replace(' ', ''))
        print(price_today)


class Get_popmusic_price(Music_price):
    def __int__(self):
        web_site = 'https://pop-music.ru/products/'


class Get_mirm_price(Music_price):
    web_site = 'https://mirm.ru/catalog/products/'


# pop 'gitarnaya-radiosistema-line-6-relay-g30-888880006013/'
# mirm line_6_relay_g30