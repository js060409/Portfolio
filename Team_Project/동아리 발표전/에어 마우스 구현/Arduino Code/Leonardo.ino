#include <SoftwareSerial.h>
#include <Mouse.h>

SoftwareSerial btSerial(11, 10);
String RS; //수신된 문자열
int gyroX, gyroZ; //마우스 조종에 필요한 변수 선언
int index1, index2, index3, index4, index5; //쉼표 분리에 필요한 인덱스 변수 선언
int flex_value = 165;

void setup() {
  Serial.begin(9600);
  btSerial.begin(9600);
  Mouse.begin();
}

void loop() {
  if (Serial.available()) {

    RS = btSerial.readStringUntil('\n'); //'\n' 전까지 값 읽어서 하나의 String 생성

    //gyroX분리
    index1 = RS.indexOf(',');
    gyroX = RS.substring(0, index1).toInt();

    //gyroZ분리
    index2 = RS.indexOf(',', index1 + 1);
    gyroZ = RS.substring(index1 + 1, index2).toInt();


    if(Serial.available())
    {
      delay(5); 
      while(Serial.available())
      {
        btSerial.write(Serial.read());
      }
    }
    
    
    

    //마우스 움직이기
    Mouse.move(gyroZ, gyroX);

    
    
  }
  delay(5);
  
  if(btSerial.available())
    {
      delay(5); 
      while(btSerial.available())
      {
        Serial.write(btSerial.read());
      }
    }
}
