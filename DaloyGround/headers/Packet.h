#ifndef PACKET_H
#define PACKET_H

struct Packet {
	byte throttle;
	byte yaw;
	byte pitch;
	byte roll;
	byte aux1;
	byte aux2;
};

#endif