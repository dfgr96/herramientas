int analog_pin = 0;
void setup() {
  Serial.begin(9600);
  pinMode (2, OUTPUT);
  pinMode (3, OUTPUT);
  pinMode (4, OUTPUT);
}

void loop() {
  int valor = analogRead(analog_pin);
  Serial.println(valor);
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);

  char c=(unsigned char)(float)((analogRead(0)/900.0)*255.0);
  Serial.println((unsigned int)c);
  if(c> 50){
  digitalWrite(2,HIGH);
  if (c > 100){
  digitalWrite(3,HIGH);
  if(c>150){
  digitalWrite(4,HIGH);
  }
  }
  }
  delay(250);
}
