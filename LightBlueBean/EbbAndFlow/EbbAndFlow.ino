/////////////////////////////////////////
// Roger Meike, 2014
/////////////////////////////////////////
// This program is written for the LightBlue Bean.
// It toggles a GPIO line on and off at defined duty cycle.  It is designed 
// to control a hydroponic ebb and flow system, but could be useful
// for other things as well.
// It uses the BTLE scratch areas to report values and control the system.
// Three of the scrath areas are to report out battery level, battery voltage,
// and temperature.  An external device can get these values vi Bluetooth LE.
// Similarly, the next two scratch areas are used to set the approximate number
// of milliseconds that the I/O pin will be set high or low
/////////////////////////////////////////

//The LightBlue Bean has five scratch areas for communication over Bluetooth
static int BATTERY_LEVEL_SCTRATCH   = 1;
static int BATTERY_VOLTAGE_SCTRATCH = 2;
static int TEMPERATURE_SCTRATCH     = 3;
static int MSEC_HIGH_SCTRATCH       = 4;
static int MSEC_LOW_SCTRATCH        = 5;

static int digitalOut = 2;       // Digital I/O pin to control
boolean ledCheck = true; //set this to true if you'd like the 
                         //LED to be on when the pin is high

unsigned long msec_on = 30;     // 30 seconds
unsigned long msec_off = 120;   // 120 seconds

void setup()
{
  Serial.begin(57600);
  
  pinMode(digitalOut, OUTPUT);
  
  //set initial values for on and off times
  Bean.setScratchNumber(MSEC_HIGH_SCTRATCH, msec_on);
  Bean.setScratchNumber(MSEC_LOW_SCTRATCH, msec_off);
  
  Serial.println("Initialized");
}

void loop()
{    
  uint16_t batteryL = Bean.getBatteryLevel();
  uint16_t batteryV = Bean.getBatteryVoltage();
  int8_t temp = Bean.getTemperature();
 
  //make the battery and temp values readable
  Bean.setScratchNumber(BATTERY_LEVEL_SCTRATCH, (long)batteryL);
  Bean.setScratchNumber(BATTERY_VOLTAGE_SCTRATCH, (long)batteryV);
  Bean.setScratchNumber(TEMPERATURE_SCTRATCH, (long)temp);
  delay(1);
  
  //read the on and off values from the scratch
  msec_on = Bean.readScratchNumber(MSEC_HIGH_SCTRATCH);
  msec_off = Bean.readScratchNumber(MSEC_LOW_SCTRATCH);  
  
  //If anyone is listening report the values
  Serial.print("on: ");
  Serial.print(msec_on);
  
  //Turn on and sleep
  if (ledCheck)
    Bean.setLed(1,0,0);
  digitalWrite(digitalOut, HIGH);
  Bean.sleep(msec_on * 1000);
 
  Serial.print(", off: ");
  Serial.println(msec_off);
   
  //Turn off and sleep
  if (ledCheck)
    Bean.setLed(0,0,0);
  digitalWrite(digitalOut, LOW);
  
  Serial.print("...");
  Bean.sleep(msec_off * 1000);
}
