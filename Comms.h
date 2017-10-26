#ifndef COMMS_H
#define COMMS_H

#include <SoftwareSerial>

class Comms {
  public:
  Comms();
  Comms(int pin);

  private:
  SoftwareSerial serial;
};

#endif
