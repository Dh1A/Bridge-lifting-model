 int flag1 = 1;
 int flag2 = 1;
 int flag3 = 1;
 int flag4 = 1;
 int flag5 = 1;
 int flag6 = 1;
 
 
 volatile int impulse1 = 0;
volatile int impulse2 = 1000;
volatile int impulse3 = 2000;
volatile int impulse4 = 3000;
volatile int impulse5 = 4000;
volatile int impulse6 = 5000;

int sens1 = 2;
int sens2 = 3;
int sens3 = 18;
int sens4 = 19;
int sens5 = 20;
int sens6 = 21;

void setup() {

Serial.begin(9600);

pinMode(sens1, INPUT_PULLUP);
 pinMode(sens2, INPUT_PULLUP);
 pinMode(sens3, INPUT_PULLUP);
 pinMode(sens4, INPUT_PULLUP);
 pinMode(sens5, INPUT_PULLUP);
 pinMode(sens6, INPUT_PULLUP);




 
attachInterrupt(digitalPinToInterrupt(2), count1, HIGH);
attachInterrupt(digitalPinToInterrupt(3), count2, HIGH);
attachInterrupt(digitalPinToInterrupt(18), count3, HIGH);
attachInterrupt(digitalPinToInterrupt(19), count4, HIGH);
attachInterrupt(digitalPinToInterrupt(20), count5, HIGH);
attachInterrupt(digitalPinToInterrupt(21), count6,HIGH);
}





void count1()
{

if (flag1 == 1&& impulse1 < 300)
{
impulse1++;


}

if (flag1 == 0 && impulse1 > 0)
{
impulse1--;

}

Serial.println(impulse1);
 
}




void count2()
{

if (flag2 == 1 && impulse2 < 1300)
{
impulse2++;


}



if (flag2 == 0 && impulse2 > 1000)
{
impulse2--;

}
Serial.println(impulse2);
 
}


void count3()
{

if (flag3 == 1 && impulse3 < 2300)
{
impulse3++;


}

if (flag3 == 0 && impulse3 > 2000)
{
impulse3--;

}

Serial.println(impulse3);
 
}


void count4()
{

if (flag4 == 1 && impulse4 < 3300)
{
impulse4++;


}

if (flag4 == 0 && impulse4 > 3000)
{
impulse4--;

}
Serial.println(impulse4);
 
}


void count5()
{

if (flag5 == 1 && impulse5< 4300)
{
impulse5++;


}
if (flag5 == 0 && impulse5 > 4000)
{
impulse5--;

}
Serial.println(impulse5);
 
}



void count6()
{

if (flag6 == 1 && impulse6 < 5300)
{
impulse6++;


}
if (flag6 == 0 && impulse6 > 5000)
{
impulse6--;

}
Serial.println(impulse6);
 
}


void loop() {



if (Serial.read() == 'S')
{
  impulse1 = 0;
  impulse2 = 1000;
  impulse3 = 2000;
  impulse4 = 3000;
  impulse5 = 4000;
  impulse6 = 5000;
  }
if (Serial.read() == 'A')
{
  
  flag1 = 1;
  }
if (Serial.read() == 'B')
{
  
  flag1 = 0;
  }


if (Serial.read() == 'C')
{
  
  flag2 = 1;
  }
if (Serial.read() == 'D')
{
  
  flag2 = 0;
  }

if (Serial.read() == 'E')
{
  
  flag3 = 1;
 
  }
if (Serial.read() == 'F')
{
  
  flag3 = 0;

  }

if (Serial.read() == 'G')
{
  
  flag4 = 1;
  }
if (Serial.read() == 'H')
{
  
  flag4 = 0;
  }

if (Serial.read() == 'I')
{
  
  flag5 = 1;
  }
if (Serial.read() == 'J')
{
  
  flag5 = 0;
  }


if (Serial.read() == 'K')
{
  
  flag6 = 1;
  }
if (Serial.read() == 'L')
{
  
  flag6 = 0;
  }


}






















