import random

situation = ['비', '폭설', '공사 중' ,'맑은 날', '다중 추돌사고', ' 사고']
number = int(random.randint(0,5))
weather = situation[number]

user_answer_1 = int(input('현재 {} 상태입니다. 북도로 우회하시겠습니까?우회를 원하시면 1을 아니면 2를 선택하십시오. :  '.format(weather)))


if user_answer_1 == 1:
    print('알겠습니다.')

elif user_answer_1 == 2:
    user_answer_2 = int(input('현재 교통량이 많아 2시간 이상 예상됩니다. 그래도 고속도를 이용하시겠습니까? [1은 네, 2는 아니오]:  '))

    if user_answer_2 == 1:
        print('알겠습니다.')

    elif user_answer_2 == 2:
        print('옳은 선택입니다.')

# 처음 코드가 오류가 났던 이유
# input()은 하나의 값만 받을수 있는데 여러개를 받으려고 함
# 그래서 format 함수나 %s 사용해서 개선함
# 2023_12_17 박종상, 김건우
