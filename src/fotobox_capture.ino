#define RELAY_PIN 4

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  digitalWrite(RELAY_PIN, LOW);
  digitalWrite(LED_BUILTIN, HIGH);
}

void loop() {
  if (Serial.available() > 0) {
    if (Serial.read() == 'c') {
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(RELAY_PIN, HIGH);
      delay(1000);
      digitalWrite(RELAY_PIN, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
  }
}
