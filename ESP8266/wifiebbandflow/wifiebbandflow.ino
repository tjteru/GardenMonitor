

#include <ESP8266WiFi.h>
#include "auth.h"
WiFiClient client;

void setup() {  // put your setup code here, to run once:
  Serial.begin(9600);
  WiFi.begin(ID_SSID, ID_PSWD);
  while (WiFi.status() != WL_CONNECTED ) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

}

void loop() {
  const int httpPort = 80;
  if (!client.connect("data.sparkfun.com", httpPort)) {
    Serial.println("connection failed");
    return;
  }
  float humidity = 97.0;
  int pump = 0;
  float solarwatts = 7.0;
  float temperature = 23;
  client.print("GET /input/");
  client.print(ID_PUBLICKEY);
  client.print("?private_key=");
  client.print(ID_PRIVATEKEY);
  client.print("&humidity=");
  client.print(humidity);
  client.print("&pump=");
  client.print(pump);
  client.print("&solarwatts=");
  client.print(solarwatts);
  client.print("&temperature=");
  client.print(temperature);
  client.print("\r\n HTTP/1.0\r\n\r\n");
  Serial.println("sent command");
  client.stop();
  delay(60000);
}
