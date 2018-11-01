#include <Wire.h>
#include <SparkFun_MS5803_I2C.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS A0

#define ADDRESS 0x77
#define PH_PIN A1
#define SAMPLE_SIZE 40
#define SAMPLING_INTERVAL 20


//MS5803 ms(ADDRESS);
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

float temp=30;
double abs_pressure=101325, pH=7;

long timeCache = -1;
long pHSum = 0;
int sampleCount = 0;

bool relayOpen = true;

void getPH() {
  if (timeCache < 0) {
    timeCache = millis();
  }
  if (millis() - timeCache > SAMPLING_INTERVAL) {
    int pHVal = analogRead(PH_PIN);
    sampleCount++;
    if (sampleCount < SAMPLE_SIZE) {
      pHSum += pHVal;
    } else {
      sampleCount = 0;
      pH = (double) pHSum;
      pH /= SAMPLE_SIZE;
      pHSum = 0;
      double voltage = (pH * 5.0) / 1024;
      pH = 3.5 * voltage;
    }
  }
}

void setup() {
  Serial.begin(9600);
//  Serial.println(1);
//  ms.reset();
//  Serial.println(2);
//  ms.begin();
//  Serial.println(3);
  pinMode(4, OUTPUT);
  sensors.begin();

//  pressure_baseline = ms.getPressure(ADC_4096);
//  Serial.println("exited setup");
}

void loop() {
  if (Serial.available()) {
    String receivedSignal = Serial.readStringUntil('\n');
    receivedSignal.trim();
    Serial.print("Received input: ");
    Serial.print("(");
    Serial.print(receivedSignal.length());
    Serial.print(") ");
    Serial.println(receivedSignal);

    if(receivedSignal == "CLOSE"){
      relayOpen = true;
      digitalWrite(4, LOW);
    } else if(receivedSignal == "OPEN"){
      relayOpen = false;
      digitalWrite(4, HIGH);
    } 
  }
//  getPH();
  sensors.requestTemperatures();
  temp = sensors.getTempCByIndex(0);
  String data = "";
  data += temp;
  data += ",";
  data += abs_pressure;
  data += ",";
  data += pH;
  data += "\n";
  Serial.print(data);
}
