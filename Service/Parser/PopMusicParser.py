from Service.Parser.MainParser import MainParser
class PopMusicParser(MainParser):
    def __init__(self):
        self.web_site = 'https://pop-music.ru/products/'
        self.find_class = 'productfull__newprice'

    def __str__(self):
        return "pop"