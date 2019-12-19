import random

name=['홍길동','희동이','둘리']
eng_name={
    '홍길동':'hong',
    '희동이':'dong',
    '둘리':'twolee'
}

selected = random.choice(name)
selected_eng = eng_name[selected]

intro = '저는 {}입니다. My name is {}.'.format(selected,selected_eng)
intro2 = f'저는 {selected}입니다. My name is {selected_eng}.'

print(intro)
print(intro2)
