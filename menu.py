import random

phone_book = {
    '새마을식당':'111-111',
    '멀캠20층':'222-222',
    '홍콩반점':'333-333',
    '순남시래기':'444-444'
}

print(phone_book['새마을식당'])

menu = ['1','2','3','4','5']

lunch = random.choice(menu)

print(lunch)