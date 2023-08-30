import telegram_sender
from Service.Parser.MainParser import MainParser
from Service.Parser.MirmParser import MirmParser
from Service.Parser.PopMusicParser import PopMusicParser
from Service.Parser.DjStoreParser import DjStoreParser


popmusic = PopMusicParser()
telegram_sender.send_message(
    f"Pop Music price: {popmusic.get_price_by_item('gitarnaya-radiosistema-line-6-relay-g30-888880006013/')[0].text}")

mirm = MirmParser()
telegram_sender.send_message(
    f"Mir Music price: {mirm.get_price_by_item('line_6_relay_g30')[0].text}")

# djstore = DjStoreParser()
# telegram_sender.send_message(
#     f"Pop Music price: {djstore.get_price_by_item('mikrofony/radiosistemy_instrumentalnye/3456_line-6-relay-g30.html')[0].text}")



