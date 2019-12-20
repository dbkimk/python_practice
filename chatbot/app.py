# import telegram

from flask import Flask
import requests
from decouple import config


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world!'


api_url = 'https://api.telegram.org'
token = config('TOKEN')
chat_id = config('CHAT_ID')

text = 'hello'

@app.route('/send/<text>')
def send(text='hello'):
    res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return 'ok!'


app.run(debug=True)