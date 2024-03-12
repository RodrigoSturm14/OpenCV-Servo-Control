#include <Servo.h>

#define LED_BUILTIN 13
#define PIN_SERVO 9
#define TICK_LED 1500

Servo servoMotor;

int newMillis = 0;
String incomingString;

void setup() {
  Serial.begin(9600);
  Serial.println("iniciando");
  pinMode(LED_BUILTIN, OUTPUT);
  servoMotor.attach(PIN_SERVO);
}

void loop() {
  // Serial.available() devuelve la cantidad de bytes q se recibio --> si se recibio algo entra en if para leer los bytes
  while(Serial.available() > 0){
    incomingString = Serial.readStringUntil('\n');
    Serial.print("Message: ");
    Serial.println(incomingString);
  }
  Serial.println(incomingString);
  // en el final de incomingString no tiene \n
  if(incomingString == "center"){ 
    digitalWrite(LED_BUILTIN, HIGH);
    servoMotor.write(90);
    Serial.print("Moviendo al Centro");
  }

  else if(incomingString == "right"){
    digitalWrite(LED_BUILTIN, LOW);
    servoMotor.write(0);
    Serial.print("Moviendo a la derecha");
  }

  else if(incomingString == "left"){
    digitalWrite(LED_BUILTIN, LOW);
    servoMotor.write(180);
    Serial.print("Moviendo a la izquierda");
  }


  // else if(millis() >= newMillis + TICK_LED){
  //   newMillis = millis();
  //   digitalWrite(LED_BUILTIN, LOW);
  // }

  
}
