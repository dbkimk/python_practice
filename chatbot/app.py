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
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

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
    elif text[0:3]=='번역 ':
        to_be_translated = text[3:]
        # https://github.com/naver/naver-openapi-guide/blob/master/sample/python/APIExamTranslateNMT.py
        url='https://openapi.naver.com/v1/papago/n2mt'
        headers = {
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Naver-Client-Id': naver_client_id,
            'X-Naver-Client-Secret': naver_client_secret
        }
        data = f'source=ko&target=en&text={to_be_translated}'.encode('utf-8')
        response = requests.post(url,headers=headers,data=data).json()
        response =  response.get('message').get('result').get('translatedText')
    else:
        response = f'너는 {text}라고 보냈는데, 너가 할 줄 아는 건 메뉴야'
    
    res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={response}')
    return 'ok',200

@app.route('/translate/<text>')
def translate(text):
    to_be_translated = text
    # https://github.com/naver/naver-openapi-guide/blob/master/sample/python/APIExamTranslateNMT.py
    url='https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret
    }
    data = f'source=ko&target=en&text={to_be_translated}'.encode('utf-8')
    response = requests.post(url,headers=headers,data=data).json()
    translated = response.get('message').get('result').get('translatedText')
    res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text=Input: {text}\nOutput: {translated}')
    return f'Input: {text}\nOutput: {translated}'

app.run(debug=True)


'''
# TELEGRAM BOT

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
'''

