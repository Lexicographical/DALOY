#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8);
const byte address[6] = "000001";

void setup() {
  Serial.begin(250000);
  radio.begin();
  radio.setAutoAck(false);
  radio.setDataRate(RF24_250KBPS);
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
  Serial.println(RF24_PA_MIN);
  Serial.println(RF24_PA_MAX);
}

void loop() {
  Serial.print("Checking...");
  if (radio.available()) {
    Serial.println("Yes");
    char text[32] = "";
    radio.read(&text, sizeof(text));
    Serial.println(text);
  } else {
    Serial.println("No");
  }
  delay(100);
}
