import requests
from bs4 import BeautifulSoup
import telegram_sender

def get_price(parser, product):
    web_site_text = requests.get(parser.web_site + product).text
    soup = BeautifulSoup(web_site_text, 'html.parser')
    return soup.find(class_=parser.find_class).text
     
today_price = get_price(MimrParser(), 'line_6_relay_g30')
telegram_sender.send_message(today_price)
today_price = get_price(PopMusicParser(), 'gitarnaya-radiosistema-line-6-relay-g30-888880006013')
telegram_sender.send_message(today_price)
