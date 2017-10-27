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
};

#endif
