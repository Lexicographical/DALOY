#include <DHT.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085_U.h>

//#define DEBUG
int DHTPIN = A2;

#ifndef DEBUG
  Adafruit_BMP085_Unified bmp = Adafruit_BMP085_Unified(10085);
  DHT dht(DHTPIN, DHT11); 
#endif

float hum, alt, temp, pressure;

void setup()
{
  Serial.begin(9600);
  #ifndef DEBUG
    dht.begin();
    bmp.begin();
  #endif
}

void loop()
{
  #ifndef DEBUG
    bmp.getPressure(&pressure);
    bmp.getTemperature(&temp);
    hum = dht.readHumidity();
    alt = bmp.pressureToAltitude(101325, pressure);
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
  data += pressure;
  data += ",";
  data += alt;
  data += "\n";

  Serial.print(data);
  
  delay(500);
}
