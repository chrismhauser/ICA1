/*
I am using the Energia IDE and the redbear WiFi Mini
 */


byte i;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  i=0;
}

// the loop routine runs over and over again forever:
void loop() {

  //* for in-class assignment change this to read analog
  //   signal and send on serial port to computer
  
  
  // print out the value:
  Serial.write(i);
  i += 1;
  
  if(i>=255)
    i=0;
  
  delay(10);        // delay in between reads for stability
}
