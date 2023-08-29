from Service.Parser.MainParser import MainParser
class PopMusic(MainParser):
    def __init__(self):
        self.web_site = 'https://pop-music.ru/products/'
        self.find_tag = "class_ = 'productfull__newprice'"
