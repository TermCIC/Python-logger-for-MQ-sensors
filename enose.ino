void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  int sensorValueMQ2 = analogRead(13);
  int sensorValueMQ3 = analogRead(14);
  int sensorValueMQ4 = analogRead(27);
  int sensorValueMQ5 = analogRead(26);
  int sensorValueMQ6 = analogRead(25);
  int sensorValueMQ7 = analogRead(33);
  int sensorValueMQ8 = analogRead(32);
  int sensorValueMQ9 = analogRead(35);
  int sensorValueMQ135 = analogRead(34);

  // print out the value you read:
  //Serial.print("MQ2: ");
  Serial.print(sensorValueMQ2);
  //Serial.print("\tMQ3: ");
  Serial.print(",");
  Serial.print(sensorValueMQ3);
  //Serial.print("\tMQ4: ");
  Serial.print(",");
  Serial.print(sensorValueMQ4);
  //Serial.print("\tMQ5: ");
  Serial.print(",");
  Serial.print(sensorValueMQ5);
  //Serial.print("\tMQ6: ");
  Serial.print(",");
  Serial.print(sensorValueMQ6);
  //Serial.print("\tMQ7: ");
  Serial.print(",");
  Serial.print(sensorValueMQ7);
  //Serial.print("\tMQ8: ");
  Serial.print(",");
  Serial.print(sensorValueMQ8);
  //Serial.print("\tMQ9: ");
  Serial.print(",");
  Serial.print(sensorValueMQ9);
  //Serial.print("\tMQ135: ");
  Serial.print(",");
  Serial.println(sensorValueMQ135);

  delay(1000); // delay in between reads for stability
}
