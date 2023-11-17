# 목적
자이로 센서와 블루투스 모듈을 활용한 에어 마우스 구현하기 ( 모형 총에 부착하여 게임 제작하기 )


# 개발 방법
아두이노 ( Arduino ) 를 사용하여 제작함 [ arduini 1.8.19 ]
- Unity 게임 구현 조 : ( 이도현 외 1학년 )
- 하드웨어 개발 조 : ( 강우찬, 박종상 )
  
- 2023/10/18 계획 변경 사항
- Unity 개발은 시간이 오래걸릴것으로 판단하여 비교적 적은 시간에 큰 효과를 볼수있는 엔트리 사용 결정
- 엔트리라는 가벼운 프로그램을 사용할 것인 만큼 다양한 항목들중 가장 나은 것들을 선출하여 사용할 예정


# 사용 도구
1. Arduino Leonardo
2. Arduino Nano33 IOT
3. Bluetooth HC - 05
4. 3 Axis Arduino gyro sensor


# 개발 진행도
- Unity 게임 개발 조 ( 변경 전 )
1. 사용할 에셋 발견 완료
2. 에섯 사용법 자료 탐색 완료

- unity 게임 개발 조 ( 변경 후 )
1. 엔트리 사용 가능한 인력 탐색
2. 에어 마우스 활용 게임 아이디어 구상
3. 실질적 구현 해보기


- 하드웨어 개발 조
1. 자료 탐색 완료
2. 참고 코드 발견 완료
3. 블루투스 연결 방법 확인 완료
4. 하드웨어 재 디자인 하기 ( 진행 중 )


- 선 배치
# AirMouse
Making AirMouse(wireless) with Arduino Leonardo and Arduino Uno

최종 핀 코드
자이로
VCC - 5V
GND - GND
SCL - 3
SDA - 2
INT - 7

좌클릭
GND
4

중앙 정렬용 엔터
GND
8


