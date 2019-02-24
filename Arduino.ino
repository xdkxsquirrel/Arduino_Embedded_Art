// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(7, OUTPUT);
  pinMode(8, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  if(digitalRead(8) == HIGH)
  {
    digitalWrite(7, HIGH);   // turn the LED on (HIGH is the voltage level)
  }
  else
  {
    digitalWrite(7, LOW);    // turn the LED off by making the voltage LOW
  }
}
