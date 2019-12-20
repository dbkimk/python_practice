# import telegram

from flask import Flask,request
import requests
from decouple import config
import random


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


@app.route('/chatbot',methods=['POST'])
def chatbot():
    from_telegram = request.get_json()
    chat_id = from_telegram.get('message').get('from').get('id')
    text = from_telegram.get('message').get('text')
    res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    # status code 200 -> ok 잘 접수했다

    if text=='메뉴':
        menus = ['양자강','20층','김밥카페']
        lunch = random.choice(menus)
        response = lunch
    elif text=='로또':
        lotto = random.sample(range(1,46),6)
        lotto = sorted(lotto)
        response = f'추천 로또 번호는 {lotto}'
    else:
        response = f'너는 {text}라고 보냈는데, 너가 할 줄 아는 건 메뉴야'
    
    res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={response}')
    return 'ok',200

app.run(debug=True)