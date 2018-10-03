#include <Arduino.h>
#include <Wire.h>
#include <SFE_BMP180.h>
#include <DHT.h>
#include <SoftwareSerial.h>

#define DEBUG
int DHTPIN = A2;

#ifndef DEBUG
  SFE_BMP180 bmp;
  DHT dht(DHTPIN, DHT11); 
#endif

SoftwareSerial XBee(2,3);

float hum, heatIndex;
double temp, pressure;

void setup()
{
  Serial.begin(9600);
  XBee.begin(9600);
  #ifndef DEBUG
    dht.begin();
    bmp.begin();
  #endif
}

void loop()
{
  #ifndef DEBUG
    queryBMP();
    hum = dht.readHumidity();
    heatIndex = dht.computeHeatIndex(temp, hum, false);
  #endif

  #ifdef DEBUG
    temp = 1;
    hum = 2;
    heatIndex = 3;
    pressure = 4;
  #endif

  String data = "";
  data += temp;
  data += ",";
  data += hum;
  data += ",";
  data += heatIndex;
  data += ",";
  data += pressure;
  data += "\n";

  XBee.print(data);
  Serial.println(data);
  
  delay(500);
}

#ifndef DEBUG
  void queryBMP() {
    char status = bmp.startTemperature();
    delay(status);
    status = bmp.getTemperature(temp);
    if (status == 0) {
  //    Serial.println("Error getting temperature!");
    }
    status = bmp.startPressure(3);
    delay(status);
    status = bmp.getPressure(pressure, temp);
    if (status == 0) {
  //    Serial.println("Error getting pressure!");
    }
  }
#endif
