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
  Sensors(int pinDHT, int pinRX, int pinTX);
  void readData();
  float getHumidity();
  float getTemperature();
  float getHeatIndex();
  float getPressure();
  bool isDHTReady();
  
private:
  Adafruit_BMP085_Unified *bmp;// = Adafruit_BMP085_Unified(10085);
  SoftwareSerial *bt;
  DHT *dht;
  float hum;
  float temp;
  float heatIndex;
  float pressure;
  bool toggleDHT;
};

Sensors::Sensors(int pinDHT, int pinRX, int pinTX) {
  this->bmp = &Adafruit_BMP085_Unified(10085);
  this->bt = &SoftwareSerial(pinTX, pinRX);
  this->dht = &DHT(pinDHT, DHT22);
}

Sensors::readData() {
  
}

#endif
