from Service.Database.JsonDatabaseLink import JsonDataBaseLink
from Service.Parser.ParserLink import parser_link
from Service.Parser.MainParser import MainParser
import telegram_sender
import os

jsdb = JsonDataBaseLink()
datebase = jsdb.datebase

for parsers, find_object in datebase['find_object']['parsers'].items():
    parser = parser_link[parsers]
    current_price = int(''.join(filter(str.isdigit, parser.get_price_by_item(find_object)[0].text)))
    datebase["find_object"]["price_history"].append(current_price)

    minimal_price = datebase["find_object"]["minimal_price"]
    if current_price < minimal_price:
        telegram_sender.send_message(
            f'Цена на {datebase["find_object"]["name"]} изменилась\n{minimal_price} >>> {current_price}\nМагазин: {parsers}')
        datebase["find_object"]["minimal_price"] = current_price
        datebase["find_object"]["minimal_price_shop"] = parsers
jsdb.save()
telegram_sender.send_message(f'---')
