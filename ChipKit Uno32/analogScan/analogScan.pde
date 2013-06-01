/*
 AnalogScan.c

 Use ChipKit Uno32 to the scan 12 analog sources and report them out the serial
 port as a comma delimited string.
  
 created 1 June, 2013
 Modified 1 June, 2013
 by Roger Meike (roger [at] awesomeinswhatwetotallyare [dot] com)
 
 This code is in the public domain.  I hereby grant a nonexclusive worldwide
 license to use this code for any purpose.  No warranty expressed or implied.

 */
 
// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPinStart = A0;  // Analog input pin that the potentiometer is attached to
const int analogInPinEnd = A11;  // Analog input pin that the potentiometer is attached to
const int millisPerSecond = 1000;
 
int sensorValue;
int interval = 10; // number of seconds between samples
unsigned long count = 0L;
unsigned long tiggerTime;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(115200); 
  tiggerTime = millis();
}

void loop() {
  // Increment the sample count.  Note this count will be reset to 0 every time the system resets 
  // or when the counter wraps.  It is only to be used to hint that data may be missing or that 
  // the system was reset.
  Serial.print(count++);
  
  // cycle through the inputs and read the analog in values:
  for (int i = 0; i <= (analogInPinEnd - analogInPinStart); i++ ) {
    sensorValue = analogRead(analogInPinStart + i);  
    
    //add each value to the comma delimited line
    Serial.print( ", " );
    Serial.print(sensorValue);                       
  }
  
  //add a carriage return
  Serial.println();

  // wait 10 seconds before the next loop
  // among other things, this allows the A/D to settle
  // after the last reading and keeps us 
  // from generating too much data
  
  delay((tiggerTime + (interval * millisPerSecond)) - millis());  
  tiggerTime = millis();  
    
}
