#ifndef SINGLETON_H
#define SINGLETON_H

#include "Constants.h"
#include "Comms.h"
#include "Comms_U.h"
#include "DroneController.h"
#include "DroneController_U.h"
#include "Sensors.h"
#include "Sensors_U.h"

class Daloy {
  public:
  static Comms* getComms();
  static DroneController* getDroneController();
  static Sensors* getSensors();
};

Comms* Daloy::getComms() {
  return Comms::getInstance();
}

DroneController* Daloy::getDroneController() {
  return DroneController::getInstance();
}

Sensors* Daloy::getSensors() {
  return Sensors::getInstance();
}

#endif
