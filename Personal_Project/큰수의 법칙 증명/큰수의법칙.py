import random                                           #랜덤 라이브러리 다운로드

num_list_1 = []                                         #랜덤으로 뽑은 숫자들을 넣을 리스트 들 1 ~ 6
num_list_2 = []
num_list_3 = []
num_list_4 = []
num_list_5 = []
num_list_6 = []

trial_count = int(input('시행 횟수를 입력하세요: '))       #사용자가 몇번 시행할지 횟수 받기(정수 형태)

for i in range(trial_count):                               #반복문
    number = random.randint(1, 6)                          #1 ~ 6까지의 수 중에 임의로 뽑음                       
    if number == 1:                                        #뽑힌 수가 1 일때
        num_list_1.append(number)                          #뽑은 숫자를 num_list_1에 추가함
                                                           #나머지는 같음
    if number == 2:
        num_list_2.append(number)

    if number == 3:
        num_list_3.append(number)

    if number == 4:
        num_list_4.append(number)

    if number == 5:
        num_list_5.append(number)

    if number == 6:
        num_list_6.append(number)

print('1이 나온 수: ', len(num_list_1))                    #1이 나온 수를 출력 (len(리스트) = 리스트의 길이)
print('2가 나온 수: ', len(num_list_2))                    #이하 같음
print('3이 나온 수: ', len(num_list_3))
print('4가 나온 수: ', len(num_list_4))
print('5가 나온 수: ', len(num_list_5))
print('6이 나온 수: ', len(num_list_6))

print('-------------------------------------------------')  #구분선

print('1이 나올 확률 = ', len(num_list_1), '/' ,trial_count)    #1이 나올 확률 = (리스트의 길이) / line 12에서 사용자가 입력한 값(시행 횟수)
print('2가 나올 확률 = ', len(num_list_2), '/' ,trial_count)    #이하 같음
print('3이 나올 확률 = ', len(num_list_3), '/' ,trial_count)
print('4가 나올 확률 = ', len(num_list_4), '/' ,trial_count)
print('5가 나올 확률 = ', len(num_list_5), '/' ,trial_count)
print('6이 나올 확률 = ', len(num_list_6), '/' ,trial_count)

from matplotlib import pyplot as plt                           #matplotlib 라이브러리에서 pyplot을 가져오고 접두사는 plt로 함
import numpy as np                                             #numpy 라이브러리가져오고 접두사 np
numbers = ['1', '2', '3', '4', '5', '6']                       #x축 값들
probablity = []                                                #y축 값 (아직 없지만 이후 다음 라인에서 값 추가 예정)

probablity.append(int(len(num_list_1)))                        #probablity 리스트에 num_list_1의 길이 값을 저장함 (1이 나온 총 횟수)
probablity.append(int(len(num_list_2)))                        #이하 같음
probablity.append(int(len(num_list_3)))
probablity.append(int(len(num_list_4)))
probablity.append(int(len(num_list_5)))
probablity.append(int(len(num_list_6)))


plt.figure(dpi = 200)                                         #해상도 조절
plt.figure(figsize=(10, 5))                                   #그래프 사이즈 조절
plt.rc('font', family = 'NanumGothic')                        #그래프 적용 글씨체
plt.title('큰수의 법칙 증명 결과')                            #그래프 제목
plt.bar(numbers, probablity, color = 'blue')                  #그래프 그리기
plt.show()                                                   #그래프 나타내기

#-----------------------------------------------------------------------------------
# idea was supplied by 'Jinjimearong'
# 확률과 통계 단원에서 큰수의 법칙과 관련된 증명
# 테스트 결과 (2023_07_25) : 성공
