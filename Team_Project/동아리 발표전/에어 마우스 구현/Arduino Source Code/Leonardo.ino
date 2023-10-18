#include <SoftwareSerial.h>
#include <Mouse.h>

SoftwareSerial mySerial(11, 10);
String RS; //수신된 문자열
int gyroX, gyroZ; //마우스 조종에 필요한 변수 선언
int index1, index2, index3, index4, index5; //쉼표 분리에 필요한 인덱스 변수 선언
int flex_value = 165;

void setup() {
  Serial.begin(9600);
  mySerial.begin(38400);
  Mouse.begin();
  Serial.println("ATcommand");
}

void loop() {
  if (mySerial.available()) {

    RS = mySerial.readStringUntil('\n'); //'\n' 전까지 값 읽어서 하나의 String 생성

    //gyroX분리
    index1 = RS.indexOf(',');
    gyroX = RS.substring(0, index1).toInt();

    //gyroZ분리
    index2 = RS.indexOf(',', index1 + 1);
    gyroZ = RS.substring(index1 + 1, index2).toInt();

  

    Serial.print("GYROX : ");
    Serial.print(gyroX);
    Serial.print(", GYROZ : ");
    Serial.print(gyroZ);

    if (mySerial.available()) {       
    Serial.write(mySerial.read());  //블루투스측 내용을 시리얼모니터에 출력
    }
    if (Serial.available()) {         
    mySerial.write(Serial.read());  //시리얼 모니터 내용을 블루추스 측에 WRITE
    }
    
    

    //마우스 움직이기
    Mouse.move(gyroZ, gyroX);

    
    
  }
  delay(5);
}
