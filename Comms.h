#ifndef COMMS_H
#define COMMS_H

#include <ESP8266Wifi.h>
#include <ESP8266WebServer.h>

class Comms {
  public:
  static Comms getInstance();
  void handleClient();
  void webHandler();

  private:
  Comms();
  static Comms* instance = 0;
  ESP8266WebServer* server;
  const char* ssid = "Daloy";
  const char* password = "Daloy";
};

#endif
