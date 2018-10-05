#ifndef COMMS_H
#define COMMS_H

class Comms {
  public:
	static Comms* getInstance() {
		static Comms instance;
		return &instance;
	}

  private:
	Comms();
	void send(Packet packet);
	RF24* radio;
	unsigned long currentMillis;
	unsigned long prevMillis;
};

#endif
