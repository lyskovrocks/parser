from Service.Parser.MainParser import MainParser
class MirmParser(MainParser):
    def __init__(self):
        self.web_site = 'https://mirm.ru/catalog/products/'
        self.find_tag = "id='results-price'"