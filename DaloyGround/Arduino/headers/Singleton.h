#ifndef SINGLETON_H
#define SINGLETON_H

#include "Comms.h"
#include "Comms_U.h"
#include "Packet.h"

class Daloy {
  public:
  static Comms* getComms();
};

Comms* Daloy::getComms() {
  return Comms::getInstance();
}

#endif
