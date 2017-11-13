
int Cons = 0; 
 volatile int impulse = 0;
int sensorius = 2;
int cons = 0;
int impulsenum = 0;
void setup() {
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
Serial.begin(9600);
pinMode(sensorius, INPUT_PULLUP); 
attachInterrupt(digitalPinToInterrupt(2), count, CHANGE);

}





void count()
{
impulse++;

Serial.println(impulse);

  
}



void Avant()

{
  digitalWrite(6,HIGH);
  digitalWrite(7,LOW);
  
  
  }

void Arriere()

{
  digitalWrite(7,HIGH);
  digitalWrite(6,LOW);
  
  }

void Stop()
{
  digitalWrite(7,LOW);
  digitalWrite(6,LOW);
  
  
  }



void loop() {

 Arriere();
}






















