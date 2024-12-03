#include <Servo.h>

Servo servo1; //hip
Servo servo2; //knee
Servo servo3; //foot
int mode = 0;
int knee;
int hip;
int foot;

void setup() {
  // put your setup code here, to run once:
  servo1.attach(1); // standing position 130; foward max 40; back max 180
  servo2.attach(2); // rpick up position 0; rest 30
  servo3.attach(3); //rest position 1400;

  servo1.write(130);
  servo2.write(30);
  servo3.write(140);
  delay(1000);
}

void loop() {
  bool walk_start_done = false;
  while(mode == 0){
    //move servo 1 and 2 and 3, back motion; 3 shoukld be allign with thigh
    //will do if it is the first time the leg is walking
    if(walk_start_done == false){
      knee = 30; hip = 130; foot = 140;
      while(knee >= 0 || hip <= 180 || foot >= 80){
        if(knee >= 0){
          servo2.write(knee);
          knee--;
        }
        if(hip >= 0){
          servo1.write(hip);
          hip++;
        }
        if(foot >= 80){
          servo3.write(foot);
            foot--;
          }
        delay(5);
      }
      walk_start_done = true;
    }
    //-----------------start of the walking loop -----------------------------
    //move servo1 foward for servo 2 extention; move servo 1 to 120
    //hip is currently 180
    while(hip >= 120){
      servo1.write(hip);
      hip--;
      delay(5);
    }
    //extend servo 2 while moving motor 1 and 3
    //hip current 120; knee current 0; foot current 110
    //foot will need to be end at rest which is 140
    //hip will need to end at foward extended which is 40
    //knee will need to be allign with upper leg which is 100
    while(foot <= 140 || hip >= 40 || knee <= 100){
      if(foot <= 140){
        servo3.write(foot);
        foot++;
      }
      if(hip >= 40){
        servo1.write(hip);
        hip--;
        }
      if(knee <= 100){
        servo2.write(knee);
        knee++;
      }
      delay(5);
    }
    //move hip back to line upper and lower leg 
    //hip current is 40
    //hip will move to 70 before moving foot
    hip = 40;
    while(hip <= 70){
      servo1.write(hip);
      hip++;
      delay(5);
    }
    
    //hip current 70
    //foot current 140; needs to be at 180
    //hip current 40; needs to be at 80
    while(foot <= 180 || hip <= 100){
      if(foot <= 180){
        servo3.write(foot);
        foot++;
      }
      if(hip <= 100){
        servo1.write(hip);
        hip++;
      }
      delay(5);
    }
    //return back to start of walking loop
    while(knee >= 0 || hip <= 180 || foot >= 80){
        if(knee >= 0){
          servo2.write(knee);
          knee--;
        }
        if(hip >= 0){
          servo1.write(hip);
          hip++;
        }
        if(foot >= 80){
          servo3.write(foot);
            foot--;
          }
        delay(5);
    }
  }
}
