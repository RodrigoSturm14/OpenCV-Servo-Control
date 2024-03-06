#define LED_BUILTIN 2
#define TICK_LED 1500
int newMillis = 0;
String incomingString;

void setup() {
  Serial.begin(115200);
  Serial.println("iniciando");
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Serial.available() devuelve la cantidad de bytes q se recibio --> si se recibio algo entra en if para leer los bytes
  while(Serial.available() > 0){
    incomingString = Serial.readStringUntil('\n');
    Serial.print("Message: ");
    Serial.println(incomingString);
  }
  Serial.println(incomingString);

  if(incomingString == "center"){
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.print("Moviendo al Centro");
  }

  else if(incomingString == "right"){
    digitalWrite(LED_BUILTIN, LOW);
    Serial.print("Moviendo a la derecha");
  }


  // else if(millis() >= newMillis + TICK_LED){
  //   newMillis = millis();
  //   digitalWrite(LED_BUILTIN, LOW);
  // }

  
}
