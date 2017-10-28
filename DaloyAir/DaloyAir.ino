#include "headers/Singleton.h"

Comms* comms;
DroneController* dc;
Sensors* sensors;

void setup() {
  Serial.begin(9600);
  Serial.print("Initializing Comms... ");
  comms = Daloy::getComms();
  Serial.println("Done");
  Serial.print("Initializing Drone Controller... ");
  dc = Daloy::getDroneController();
  Serial.println("Done");
  Serial.print("Initializing Sensors... ");
  sensors = Daloy::getSensors();
  Serial.println("Done");
}

void loop() {

}
