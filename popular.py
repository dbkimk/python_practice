import requests
import bs4

html = requests.get('https://www.naver.com')
soup = bs4.BeautifulSoup(html.text,'html.parser')

keywords = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

real_keywords = keywords[0:20]

'''
for keyword in real_keywords:
    print(keyword.text)
'''

numbers = [i for i in range(0,101)]
even_numbers = [i*2 for i in range(0,51)]

numbers2 = []

for i in range(0,101):
    numbers2.append(i)

# print(numbers2)

real_real_keywords = [keyword.text for keyword in real_keywords]

problem = sorted(real_real_keywords)

print('choose from below')
print(problem)
answer = input('Your answer: ')

if answer == real_real_keywords[0]:
    print('correct')
else:
    print('wrong')
