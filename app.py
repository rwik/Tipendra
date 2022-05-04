from http import client
from urllib import response
from flask import Flask, request
from twilio.rest import Client
from marketstack_logic import get_stock_price

import os

app = Flask(__name__)
ACC_ID = os.environ.get('')
TWI_TOKEN = os.environ.get('')
client = Client(ACC_ID, TWI_TOKEN)
TWILLO_NUMBER = 'whatsapp:+14155238886'

def process_text(text):
    if text.startswith('hi'):
        return 'Tipendra welcomes you . Please type stock symbol to get stock price :  sym:<symbol>'
    elif text.startswith('sym:'):
        symbol = text.split(':')[1]
        price = get_stock_price(symbol)
        print(price)
        if price:
            return 'The price of {} is {}'.format(symbol, price[high])
        else:
            return 'Stock symbol {} not found'.format(symbol)
    else:
        return 'Type hi to get started'

def send_text(text, recipient):
    message = client.messages.create(
        to=recipient,
        from_=TWILLO_NUMBER,
        body=text
    )
    return message

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/webhook", methods=['POST'])
def webhook():
    form = request.form
    text = form['Body']
    sender = form['From']
    response = process_text(text)
    send_text(response, sender)
    return "OK",200

   

process_text(aapl)



