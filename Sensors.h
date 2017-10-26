#ifndef SENSORS_H
#define SENSORS_H

#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085_U.h>
#include <DHT.h>
#include <SoftwareSerial.h>

class Sensors {
public:
  Sensors();
  Sensors(int pinDHT);
  void readData();
  float getHumidity();
  float getTemperature();
  float getHeatIndex();
  float getPressure();
  
private:
  Adafruit_BMP085_Unified *bmp;
  DHT *dht;
  float hum;
  float temp;
  float heatIndex;
  float pressure;
  bool toggleDHT;
};

#endif
