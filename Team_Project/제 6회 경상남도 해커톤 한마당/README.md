
# 주제
탄소 중립 - 디지털 탄소 절감

# 문제 인식
나에게 온 이메일을 지우지 않을때 조차 탄소가 발생함, 컴퓨터 사용시에도 탄소가 발생함.

( https://www.hani.co.kr/arti/science/science_general/971240.html )

# 해결 방안 제시
컴퓨터 사용은 불가피함, 그래서 컴퓨터를 사용할때 만큼이라도 탄소를 줄이도록 유도하는 OS 개발

# 개발 방법
1. OS 개발하기 [2023_11_03 : OS 개발의 기술 문제점으로 기각]
2. html , css로 OS와 최대한비슷한 환경 구축


# 사용 도구
1. 노트북
2. html
3. css

# 개발 세부 내용
1. 바탕화면에 넣을 요소들
   a. 프로필 위젯
   
   b. 랭킹 시스템 도입
     - 상위권에게는 추가 포인트 제공
   
   c. 탄소 포인트 환전
     - 교통카드 시스템과 연계
       
   d. 뱃지 시스템
     - 수집 요소, 뱃지 획득시 포인트 지급
  
   e. 탄소 절감 체크리스트

   f. 도메인 사용

# 개발 진행도
## a. 프로필 위젯
![profile](https://github.com/js060409/Portfolio/assets/101975257/f985ab67-814c-4f6c-822f-0f284f8db2b0)

프로필에 들어갈 요소
- 닉네임
- 줄인 탄소 량
- 심은 나무 그루 수 (탄소를 바탕으로 계산 5.6kg = 1그루)
이미지 및 닉네임은 임시로 경상남도 교육청 사진 및 이름 사용

## b. 랭킹 시스템
![캡처](https://github.com/js060409/Portfolio/assets/101975257/96bc6cb3-08cf-4508-927b-8a72009a6e45)

위 사진은 바탕화면에서 나타날 위젯 모습, 포인트 별로 랭크를 매김

![image](https://github.com/js060409/Portfolio/assets/101975257/5a94e0ba-216b-4d35-ac1a-ab80c5db89ad)

'세계 랭킹' 버튼을 눌렀을시 나오는 창, 각 항목은 아래와 같다
- 좌측: 국가별 개인 등수 표시 (미국,한국 일본 등)
- 중앙: 세계 각 국가의 총 등수
- 우측 : 전세계적인 탄소 배출 및 절감 비율

## c. 탄소 포인트 환전
![image](https://github.com/js060409/Portfolio/assets/101975257/f34d1b74-b0e5-4c0b-8141-017b38020361)

바탕화면 위젯 구현은 성공하였으나 내부 충전 과정 미구현

## d. 뱃지 시스템
![image](https://github.com/js060409/Portfolio/assets/101975257/04e1cb02-e611-40b1-9e63-d5cb04bf4c65)

바탕화면 위젯사진이며 해당 뱃지 중 하나를 누를 시 아래와 같은 창이 뜬다

![image](https://github.com/js060409/Portfolio/assets/101975257/a6b92dcf-cb86-4e60-9ca7-4b4ac3711a49)

각 뱃지별 설명이 나타나는 도감 형식
저탄고지의 뜻은 탄소를 줄이고 지구를 생각하다 (고지 = 생각할 '고' , '지' 구 )

## e. 탄소 절감 체크리스트
![image](https://github.com/js060409/Portfolio/assets/101975257/4622624d-33ba-43cc-bac1-9503288b374b)

일반적인 체크리스트의 형태로, 매일 12시에 초기화 되도록 설계 ( 초기화 기능 미구현 )
체크리스트 미션 완료 시 포인트 지급 기획 
( c  에서 사용 가능 )

## f. 완성한 html 코드 웹 호스팅으로 만들기 
**주소 : zerocarbonos.kro.kr  /  carbonzeroos.kro.kr **

![image](https://github.com/js060409/Portfolio/assets/101975257/3097f041-3fb0-4f6c-a4e0-e1957aeb9b83)

# 결과
바탕화면 사진
![image](https://github.com/js060409/Portfolio/assets/101975257/e067c088-4cfb-476f-abdf-80ae48e8fda6)

# 기대 효과
일상 생활에서 탄소 사용을 줄여 탄소 중립을 실천 할 수 있음

# 추가 기획 사항
pc os에만 국한 되지 않고 모바일 기기 이식하기 
- 만보기 기능, 교통카드 사용 기능 활용해서 추가 포인트 지급 방법으로 사용
html,css로만 만들지 않고 진짜 OS 제작 해보기

# 발표 자료
- 우드락
  
![image](https://github.com/js060409/Portfolio/assets/101975257/76b75209-0406-4603-aca5-4e5d0800c0f7)

- 영상 자료
  
 [https://cafe.naver.com/2020ohf](https://drive.google.com/file/d/1eEiQdWKZA6MMEqvkBkS8BzsynBjyt9OR/view?usp=sharing)https://drive.google.com/file/d/1eEiQdWKZA6MMEqvkBkS8BzsynBjyt9OR/view?usp=sharing
# 결과
해커톤 우수상 수상 ( 2등 )
32팀중 2등 수상
