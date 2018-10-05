#ifndef COMMS_U
#define COMMS_U

#include <ESP8266Wifi.h>
#include <ESP8266WebServer.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

Comms::Comms() {
	this->data.throttle = 0;
	this->data.yaw = 127;
	this->data.pitch = 127;
	this->data.roll = 127;
	this->data.aux1 = 0;
	this->data.aux2 = 0;


	this->buffer = new DynamicJsonBuffer;
	this->server = new ESP8266WebServer(80);
	this->ip = new IPAddress(192, 168, 8, 1);
	this->gateway = new IPAddress(192, 168, 8, 1);
	this->subnet = new IPAddress(255, 255, 255, 0)
	this->radio = new RF24(rfpins[0], rfpins[1]);

	radio.begin();
	radio.setAutoAck(false);
	radio.setDataRate(RF24_250KBPS);
	radio.openReadingPipe(1, uuid);

	Wifi.mode(WIFI_AP);
	WiFi.softAP(SSID, password);

	WiFi.config(this->ip, this->gateway, this->subnet);
	WiFi.begin();

	this->server->on("/daloy", Comms::handler);
	this->server->begin();
}

void Comms::handler() {
	if (server.hasArg("daloy")) {
		JsonObject& root = this->buffer->createObject();
		root["temperature"] = this->temperature;
		root["humidity"] = this->humidity;
		root["pressure"] = this->pressure;
		root["altitude"] = this->altitude;
		char buffer[256];
		root.printTo(buffer, sizeof(buffer));
		server.send(200, "text/json", buffer);
	}
}

void Comms::handleClient() {
	this->server->handleClient();
}

#endif
