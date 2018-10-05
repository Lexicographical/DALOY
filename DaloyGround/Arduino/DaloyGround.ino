#include "headers/Singleton.h"

Comms* comms;

void setup() {
  Serial.begin(115200);
  Serial.print("Initializing Comms... ");
  comms = Daloy::getComms();
  Serial.println("Done");
}

void loop() {

}