#include <DHT.h>

#define DHTPIN 07
#define DHTTYPE DHT11
DHT dht(DHTPIN,DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  
}

void loop() {
  delay(10000);

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t) ){
    Serial.println("Error From the Device");
    return;
  }

  Serial.print(h);
  Serial.print(",");
  Serial.println(t);

}
