import requests

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# simple Flask demo
@app.route("/", methods=['GET'])
def welcome():
    return 'Welcom to my web'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'hello':
        reply = 'hello, dude :)'
    elif 'church' in event.message.text:
        reply = u'你的輸入中有 "church"'
    elif 'star war' in event.message.text:
        r = requests.get('http://docs.python-requests.org/en/master/')
        this_data = r.json()
        
        reply = u'名字:%s\n 身高:%s cm\n 體重:%s kg\n 生日:%s' % (this_data["name"], this_data["height"], this_data["mass"], this_data["birth_year"])
    else:
        reply = u'功能開發中，您的訊息為-%s' % event.message.text

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))

# 有這行才能直接執行 python main.py
if __name__ == "__main__":
    app.run()
