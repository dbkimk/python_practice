import requests
import bs4

html = requests.get('https://finance.naver.com/marketindex/')
# print(html.text)

soup = bs4.BeautifulSoup(html.text,'html.parser')
kospi = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(kospi.text)