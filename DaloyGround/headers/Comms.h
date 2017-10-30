#ifndef COMMS_H
#define COMMS_H

class Comms {
  public:
	  static Comms* getInstance() {
	  	static Comms instance;
	  	return &instance;
	  }
	  void handleClient();

  private:
	  Comms();
	  void handler();
	  DynamicJsonBuffer* buffer;
	  ESP8266WebServer* server;
	  IPAddress* ip;
	  IPAddress* gateway;
	  IPAddress* subnet;
	  RF24* radio;
	  Packet data;
	  float temperature;
	  float humidity;
	  float pressure;
	  float altitude;
};

#endif
