#ifndef COMMS_U
#define COMMS_U

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

const byte slaveAddress[5] = {'R','x','A','A','A'};

Comms::Comms() {
	this->radio = new radio(CE_PIN, CSN_PIN);
	this->radio->begin();
	this->radio->setDataRate(RF24_250KBPS);
	this->radio->setRetries(3, 5);
	this->radio->openWritingPipe(uuid);
}

void Comms::send(Packet packet) {
	bool res = radio.write(&packet, sizeof(packet));
	if (res) {
		Serial.println("Acknowledgement received!");
	} else {
		Serial.println("Failed to send message!");
	}
}

#endif
