import requests
from bs4 import BeautifulSoup

web_site = "https://pop-music.ru/products/gitarnaya-radiosistema-line-6-relay-g30-888880006013/"
web_site_text = requests.get(web_site).text
soup = BeautifulSoup(web_site_text, 'html.parser')
print(soup.find_all(class_ = 'productfull__newprice')[0].text)


