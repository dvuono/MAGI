#include <Ethernet.h> //Load Ethernet Library
#include <EthernetUdp.h> //Load the Udp Library
#include <SPI.h>

String analogValues; //String to contain analog values
int const numberOfInputs = 15;  
int const numberOfCalReads = 10;
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; //Assign mac address
IPAddress ip(10, 16, 2, 177); //Assign the IP Adress
unsigned int localPort = 80; // Assign a port to talk over
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; //dimensian a char array to hold our data packet
String datReq; //String for our data
int packetSize; //Size of the packet
EthernetUDP Udp; // Create a UDP Object
int n_samples = 30;
int motorPin = 22;

void setup() {
  
  Serial.begin(9600); //Initialize Serial Port 
  // set all analog pins to "input"
  for (int i = 0; i < numberOfInputs; i++) {
    pinMode(i,INPUT);}
  pinMode(motorPin, OUTPUT);
  Ethernet.begin( mac, ip); //Inialize the Ethernet
  Udp.begin(localPort); //Initialize Udp
  delay(1500); //delay
}

void loop() {
  
  packetSize =Udp.parsePacket(); //Reads the packet size
  
  if(packetSize>0) { //if packetSize is >0, that means someone has sent a request
    
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE); //Read the data request
    String datReq(packetBuffer); //Convert char array packetBuffer into a string called datReq
    
    if (datReq =="ReadData") { //Do the following if data is requested
    
      //Raise the tube holder
      digitalWrite(motorPin, HIGH);
      delay(12000);
      
      analogValues = "";
      for (int analogChannel = 0; analogChannel < numberOfInputs; analogChannel++) {
            int sensorValue = 0;
            for(int i = 0; i <= n_samples; i++){
               sensorValue += analogRead(analogChannel); 
            }
            int sensorReading = sensorValue/n_samples; //Average the sample readings
            Serial.println(sensorReading);
            analogValues += (analogChannel);
            analogValues += (" = ");
            analogValues += (sensorReading);
            analogValues +=("; ");
            //Serial.println(analogValues);
      }
      Serial.println(analogValues);
      int bufferSize = analogValues.length();
      Serial.println(bufferSize);
      char replyBuffer[bufferSize]; 
      analogValues.toCharArray(replyBuffer, bufferSize);
      Serial.println(replyBuffer);
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort()); //Initialize packet send
      Udp.print(replyBuffer); //Send the temperature data
      Udp.endPacket(); //End the packet 
      
      //Lower the tube holder
      digitalWrite(motorPin, LOW);
      delay(7000);
    }
    
//    //Calibrate the specified well
//    if(datReq.startsWith("CalibrateWell")){ //Do the following if calibration is requested
//      string wellNumber = datReq.substring(13);
//      wellNumber.trim();
//      int analogChannel = wellNumber.toInt();
//      int totalSensorReading = 0;
//      calibrationValue = "";
//      for (int iterator = 0; iterator <numberOfCalReads; iterator++){
//         totalSensorReading = analogRead(analogChannel); 
//      }
//      calibrationValue = String(totalSensorReading/numberOfCalReads);
//      Serial.println(calibrationValue);
//      int bufferSize = calibrationValue.length();
//      Serial.println(bufferSize);
//      char replyBuffer[bufferSize];
//      calibrationValue.toCharArray(replyBuffer, bufferSize);
//      Serial.println(replyBuffer);
//      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort()); //Initialize packet send
//      Udp.print(replyBuffer);  //Send the data 
//      Udp.endPacket(); //End the packet    
//    }
      
  }
  memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE); //clear out the packetBuffer array
}
