// measure optical density a 0-5 V from Carl's OD reader.
// arduino streams data to the Pi every X seconds (configured with "signalFreq").
// number of input signal is configured with "numberOfInputs"

int const numberOfInputs = 2;        // number of pins with data streams
int ODReadings[numberOfInputs];      // array to hold readings from each pin
char poke;                           // the prompt from the Pi

void setup() {
  Serial.begin(9600);
  // set all analog pins to "input"
  for (int i = 0; i < numberOfInputs; i++) {
    pinMode(i,INPUT);
  }
}

void loop() {
  if (Serial.available()) {
    poke = Serial.read();
    if (poke == '1') {
        readOD(&ODReadings[0], numberOfInputs);
        writeOD(&ODReadings[0], numberOfInputs);
    } else {
        // check again shortly for another poke
        delay(10);
    }
  }
}

void readOD(int *ODReadings, int numberOfInputs) {
  for (int i = 0; i < numberOfInputs; i++) {
    ODReadings[i] = analogRead(i);
  }
}

void writeOD(int *ODReadings, int numberOfInputs) {
  for (int i = 0; i < numberOfInputs; i++) {
    Serial.print(i);
    Serial.print(":");
    Serial.print(ODReadings[i]);
    Serial.print(",");
  }
}
