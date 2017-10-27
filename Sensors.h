#ifndef SENSORS_H
#define SENSORS_H

#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085_U.h>
#include <DHT.h>

class Sensors {
public:
  static Sensors getInstance(int pinDHT);
  void readData();
  float getHumidity();
  float getTemperature();
  float getHeatIndex();
  float getPressure();
  
private:
  Sensors(int pinDHT);
  static Sensors* instance = 0;
  Adafruit_BMP085_Unified *bmp;
  DHT *dht;
  float hum;
  float temp;
  float heatIndex;
  float pressure;
  bool toggleDHT;
};

#endif
