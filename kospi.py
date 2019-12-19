import requests
import bs4

html = requests.get('https://finance.naver.com/sise/sise_index.nhn?code=KOSPI')
# print(html.text)

soup = bs4.BeautifulSoup(html.text,'html.parser')
kospi = soup.select_one('#now_value')

print(kospi.text)