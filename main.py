import telegram_sender
from Service.Parser.MainParser import MainParser
from Service.Parser.MirmParser import MirmParser
from Service.Parser.PopMusicParser import PopMusicParser
from Service.Parser.DjStoreParser import DjStoreParser


popmusic = PopMusicParser()
mirm = MirmParser()

print(mirm.get_price_by_item('line_6_relay_g30')[0].text.replace(' ',''))
telegram_sender.send_message(
    f"Mir Music price: {mirm.get_price_by_item('line_6_relay_g30')[0].text}\n"
    f"Pop Music price: {popmusic.get_price_by_item('gitarnaya-radiosistema-line-6-relay-g30-888880006013/')[0].text}")

