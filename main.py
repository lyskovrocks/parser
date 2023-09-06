import telegram_sender
from Parser.ParserPointer import parser_pointer
from Service.Parser.MainParser import MainParser
from Service.Parser.MirmParser import MirmParser
from Service.Parser.PopMusicParser import PopMusicParser
from Service.Parser.DjStoreParser import DjStoreParser
from Service.Database.JsonDatabase import JsonDatabase

jsdb = JsonDatabase()
database = jsdb.database

for parser_str, find_name in database["find_object"]["parsers"].items():
    parser: MainParser = parser_pointer[parser_str]
    price = ''.join(filter(str.isdigit, parser.get_price_by_item(find_name)[0].text))
    last_price = database["find_object"]["last_price"]
    if int(price) < int(last_price):
        telegram_sender.send_message(
            f"Цена на {database['find_object']['name']} снизилась: {last_price} -> {price}"
        )
    database["find_object"]["last_price"] = price
    database["find_object"]["price_history"].append(price)
    if len(database["find_object"]["price_history"]) > 10:
        database["find_object"]["price_history"].pop(0)

jsdb.save()






