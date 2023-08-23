import requests
import credentials

TELEGRAM_URL = 'https://api.telegram.org/bot'
TELEGRAM_BOT_TOKEN = credentials.TELEGRAM_BOT_TOKEN
CHAT_ID = credentials.CHAT_ID

def send_message(message, chat_id=CHAT_ID, bot_token=TELEGRAM_BOT_TOKEN, tg_url=TELEGRAM_URL):
    url_request = tg_url + \
                  bot_token + \
                  '/sendMessage?' + \
                  'chat_id=' + chat_id + \
                  '&text=' + message
    requests.get(url_request)








#   https://api.telegram.org/bot6259387438:AAFm_StPghIuzcRFDZoXwRTBL_VCBELmeTw/sendMessage?chat_id=301449765&text=rerere