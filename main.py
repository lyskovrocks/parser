import telegram_sender
from Parsers.MimrParser import MimrParser
# from Parsers.MimrParser import PopMusicParser

mimr = MimrParser()
# pop = PopMusicParser()
telegram_sender.send_message(
    f"mimr price: {mimr.get_price_by_id('line_6_relay_g30')}"
    # f"popmusic price: {mimr.get_price_by_id('gitarnaya-radiosistema-line-6-relay-g30-888880006013')}"
)

