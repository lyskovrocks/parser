import telegram_sender
from Service.Parser.MainParser import MainParser
from Service.Parser.Mirm import Mirm
from Service.Parser.PopMusic import PopMusic


popmusic = PopMusic()
print(popmusic.get_price_by_item('gitarnaya-radiosistema-line-6-relay-g30-888880006013/'))




# telegram_sender.send_message(
#     f"Pop Music price: {popmusic.get_price_by_item('gitarnaya-radiosistema-line-6-relay-g30-888880006013/')}")

# mirm = Mirm()
# telegram_sender.send_message(
#     f"Mir Music price: {mirm.get_price_by_item('line_6_relay_g30')}")


