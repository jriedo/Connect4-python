

#include <Wire.h>
#include <Adafruit_MotorShield.h>

#include <Servo.h>


Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);

Servo myservo;
int SERVOPIN = 10;

int start = 0;
int target = 140;

int pos_1 = 90;
int pos_2 = 190;
int pos_3 = 285;
int pos_4 = 380;
int pos_5 = 480;
int pos_6 = 575;
int pos_7 = 675;

//delays in ms
int servo_out = 800;
int servo_in = 800;
int motor_on_pose = 800;
int motor_home = 1000;


void setup() {
  Serial.begin(9600);
  AFMS.begin();
  myMotor->setSpeed(1000);


  pinMode(6, OUTPUT);
  digitalWrite(6, HIGH);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(7, INPUT);//endanschlag
}

void loop() {
  if (Serial.available() > 0)
  {
    int data = Serial.read();
    /*
       0 - init
       1-7 - drop positions
       8 - open drawer
       9 - close drawer
    */
    if (data == '0') {
//      int flag = 1;
//      while (flag) {
//        //myMotor->step(1, FORWARD, DOUBLE);
//        flag = digitalRead(7)==HIGH;
//        digitalWrite(LED_BUILTIN, digitalRead(7));
//      }
      myMotor->release();

      myservo.attach(10);
      myservo.write(start);
      delay(1000);
      myservo.detach();
      Serial.write('0');
    }

    if (data == '1') {
      myMotor->step(pos_1, FORWARD, DOUBLE);
      delay(motor_on_pose);
      myservo.attach(SERVOPIN);
      myservo.write(target);
      delay(servo_out);
      myservo.write(start);
      delay(servo_in);
      myservo.detach();
      myMotor->step(pos_1, BACKWARD, DOUBLE);
      myMotor->release();
      delay(motor_home);
      Serial.write('1');
    }
    if (data == '2') {
      myMotor->step(pos_2, FORWARD, DOUBLE);
      delay(motor_on_pose);
      myservo.attach(SERVOPIN);
      myservo.write(target);
      delay(servo_out);
      myservo.write(start);
      delay(servo_in);
      myservo.detach();
      myMotor->step(pos_2, BACKWARD, DOUBLE);
      myMotor->release();
      delay(motor_home);
      Serial.write('2');
    }
    if (data == '3') {
      myMotor->step(pos_3, FORWARD, DOUBLE);
      delay(motor_on_pose);
      myservo.attach(SERVOPIN);
      myservo.write(target);
      delay(servo_out);
      myservo.write(start);
      delay(servo_in);
      myservo.detach();
      myMotor->step(pos_3, BACKWARD, DOUBLE);
      myMotor->release();
      delay(motor_home);
      Serial.write('3');
    }
    if (data == '4') {
      myMotor->step(pos_4, FORWARD, DOUBLE);
      delay(motor_on_pose);
      myservo.attach(SERVOPIN);
      myservo.write(target);
      delay(servo_out);
      myservo.write(start);
      delay(servo_in);
      myservo.detach();
      myMotor->step(pos_4, BACKWARD, DOUBLE);
      myMotor->release();
      delay(motor_home);
      Serial.write('4');
    }
    if (data == '5') {
      myMotor->step(pos_5, FORWARD, DOUBLE);
      delay(motor_on_pose);
      myservo.attach(SERVOPIN);
      myservo.write(target);
      delay(servo_out);
      myservo.write(start);
      delay(servo_in);
      myservo.detach();
      myMotor->step(pos_5, BACKWARD, DOUBLE);
      myMotor->release();
      delay(motor_home);
      Serial.write('5');
    }
    if (data == '6') {
      myMotor->step(pos_6, FORWARD, DOUBLE);
      delay(motor_on_pose);
      myservo.attach(SERVOPIN);
      myservo.write(target);
      delay(servo_out);
      myservo.write(start);
      delay(servo_in);
      myservo.detach();
      myMotor->step(pos_6, BACKWARD, DOUBLE);
      myMotor->release();
      delay(motor_home);
      Serial.write('6');
    }
    if (data == '7') {
      myMotor->step(pos_7, FORWARD, DOUBLE);
      delay(motor_on_pose);
      myservo.attach(SERVOPIN);
      myservo.write(target);
      delay(servo_out);
      myservo.write(start);
      delay(servo_in);
      myservo.detach();
      myMotor->step(pos_7, BACKWARD, DOUBLE);
      myMotor->release();
      delay(motor_home);
      Serial.write('7');
    }

    else if (data == '8') {
      myservo.attach(9);
      myservo.write(target);
      delay(servo_in);
      myservo.detach();
      Serial.write('8');
    }

    else if (data == '9') {
      myservo.attach(9);
      myservo.write(start);
      delay(servo_out);
      myservo.detach();
      Serial.write('9');
    }
  }
}
