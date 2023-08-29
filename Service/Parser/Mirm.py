from Service.Parser.MainParser import MainParser
class Mirm(MainParser):
    def __init__(self):
        self.web_site = 'https://mirm.ru/catalog/products/'
        self.find_tag = "id='results-price'"