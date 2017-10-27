#ifndef SINGLETON_H
#define SINGLETON_H

#include "Comms.h"
#include "Comms_U.h"
#include "DroneController.h"
#include "DroneController_U.h"
#include "Sensors.h"
#include "Sensors_U.h"

class Daloy {
  public:
  Comms getComms();
  DroneController getDroneController();
  Sensors getSensors();
}

Comms Daloy::getComms() {
  return Comms::getInstance();
}

DroneController Daloy::getDroneController() {
  return DroneController::getInstance();
}

Sensors Daloy::getSensors(int pinDHT) {
  return Sensors::getInstance(pinDHT);
}

#endif
