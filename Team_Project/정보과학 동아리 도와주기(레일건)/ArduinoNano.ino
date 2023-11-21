int currentsens, lastsens = 0;

boolean buttoninput(boolean last, int i){
    boolean current = digitalRead(i);
    if(current != last){
        delay(15);
        current = digitalRead(i);
    }
    return(current);
}

void setup() {
    pinMode(4, OUTPUT);
    pinMode(2, INPUT);
}

void loop() {
    currentsens = buttoninput(lastsens, 2);
    if(lastsens == 0 && currentsens == 1){
        digitalWrite(4, HIGH);
        delay(8);                                  // delay 값 늘릴수록 힘 쎄짐
        digitalWrite(4, LOW);
    }
    lastsens = currentsens;
}
