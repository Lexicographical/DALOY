#ifndef SENSORS_U
#define SENSORS_U

Sensors::Sensors() {
  this->bmp = new Adafruit_BMP085_Unified(10085);
  this->dht = new DHT(PIN_DHT22, DHT22);
  this->toggleDHT = true;
  this->dht->begin();
  this->bmp->begin();
  delay(1000);
}

void Sensors::readData() {
  this->bmp->getPressure(&this->pressure);
  this->bmp->getTemperature(&this->temp);
  if (this->toggleDHT) {
    this->hum = this->dht->readHumidity();
    this->heatIndex = this->dht->computeHeatIndex(this->temp, this->hum, false);
    this->toggleDHT = false;
  } else {
    this->toggleDHT = true;
  }
}

float Sensors::getHumidity() {
  return this->hum;
}

float Sensors::getTemperature() {
  return this->temp;
}

float Sensors::getHeatIndex() {
  return this->heatIndex;
}

float Sensors::getPressure(){
  return this->pressure;
}
#endif
