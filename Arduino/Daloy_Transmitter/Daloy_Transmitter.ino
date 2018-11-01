#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8);
const byte address[6] = "000001";

void setup() {
   Serial.begin(9600);
   radio.begin();
   radio.setAutoAck(false);
   radio.setDataRate(RF24_250KBPS);
   radio.setPALevel(RF24_PA_MAX);
   radio.openWritingPipe(address);
   radio.stopListening();
}

void loop() {
  const char text[] = "Hello World!";
  int status = radio.write(&text, sizeof(text));
  Serial.print("Wrote text: ");
  Serial.println(text);
  Serial.println(status ? "Success" : "Failed");
  delay(100);
}
