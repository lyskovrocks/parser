import requests
from bs4 import BeautifulSoup
import telegram_sender
def get_price_from_popmusic(product):

    web_site = 'https://pop-music.ru/products/'
    find_product = product

    web_site_text = requests.get(web_site + find_product).text
    soup = BeautifulSoup(web_site_text, 'html.parser')
    price_today = soup.find(class_='productfull__newprice').text
    return price_today

telegram_sender.send_message(get_price_from_popmusic('gitarnaya-radiosistema-line-6-relay-g30-888880006013/'))