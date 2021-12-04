// This #include statement was automatically added by the Particle IDE.
#include <Particle-GPS.h>
#include <MQ135.h>
#include <Wire.h>


//Initialise Ports and Declare Variables
int Analog_Input = A0;
float co2, co2ppm;
String latitude, longitude, altitude, ppm;

//Specify what data comes from what sensor
MQ135 mq135(Analog_Input);
Gps _gps = Gps(&Serial1);
Timer _timer = Timer(1, onSerialData);


void setup() {
    delay(2000);
    //Set Particle Variables
    Particle.variable("ppm", ppm);
    Particle.variable("latitude", latitude);
    Particle.variable("longitude", longitude);
    Particle.variable("altitude", altitude);

    //Start Serial 1 9600 Baud
    Serial.begin(9600);
    _gps.begin(9600);
    _timer.start();
    _gps.sendCommand(PMTK_SET_NMEA_OUTPUT_ALLDATA);
}

//Required for GPS
void onSerialData()
{
  _gps.onSerialData();
}


void loop() {

  //Get Reading from MQ135 Sensor & Publish to Particle
  co2 = mq135.getPPM();
  co2ppm = co2/100;
  ppm = String(co2ppm);

  //Declare we're looking for Global Positioning Data and Parse the Data
  Gga gga(_gps);
  if (gga.parse())
  {
    //Pull out the required GPS Data and write to variables (as String)

    //Serial Outputting for Debugging
    //------------------------------
    //Serial.println("2) Global Positioning System Fixed Data ($GPGGA)");
    //Serial.println("======================================================");
    //Serial.print("UTC Time: "); Serial.println(gga.utcTime);
    //Serial.print("Latitude: "); Serial.println(gga.latitude);
   // Serial.print("North/SouthIndicator: "); Serial.println(gga.northSouthIndicator);
   // Serial.print("Longitude: "); Serial.println(gga.longitude);
   // Serial.print("East/WestIndicator: "); Serial.println(gga.eastWestIndicator);
   // Serial.print("Position Fix Indicator: "); Serial.println(gga.positionFixIndicator);
   // Serial.print("Satellites Used: "); Serial.println(gga.satellitesUsed);
   // Serial.print("Horizontal Dilution of Precision: "); Serial.println(gga.hdop);
   // Serial.print("Altitude: "); Serial.print(gga.altitude); Serial.print(" "); Serial.println(gga.altitudeUnit);
   // Serial.print("Geoidal Separation: "); Serial.print(gga.geoidalSeparation); Serial.print(" "); Serial.println(gga.geoidalSeparationUnit);
   // Serial.print("Age of Diff. Corr.: "); Serial.println(gga.ageOfDiffCorr);
   // Serial.println("");
   // Serial.print("PPM: "); Serial.print(ppm);
   // Serial.print("Data[0] = "); Serial.println(_gps.data[0]);
   // Serial.print("Data[1] = "); Serial.println(_gps.data[1]);
   // Serial.print("Data[2] = "); Serial.println(_gps.data[2]);
   // Serial.print("Data[3] = "); Serial.println(_gps.data[3]);
   // Serial.print("Data[4] = "); Serial.println(_gps.data[4]);
   // Serial.print("Data[5] = "); Serial.println(_gps.data[5]);
   // Serial.print("Data[6] = "); Serial.println(_gps.data[6]);

    //Output the N/S and W/E Indicator with the latitude/longitude value
    latitude = String((gga.northSouthIndicator) + (gga.latitude));
    longitude = String((gga.eastWestIndicator) + (gga.longitude));
    altitude = String((gga.altitude)) + (gga.altitudeUnit);

    //This checks if data is empty, and if it is, cancels and doesn't send the data.
    if (latitude == NULL){
        exit;
    if (latitude == NULL){
        delay(15000);
        return;
    }
    //Publish GPS Data to Particle in consolidated JSON
    Particle.publish("PARTICLE-DATA", String::format("{\"latitude\":\"%s\",\"longitude\":\"%s\",\"altitude\":\"%s\",\"ppm\":\"%s\"}", latitude.c_str(), longitude.c_str(), altitude.c_str(), ppm.c_str()), PRIVATE);
  }
  // Wait 15 Seconds
  delay(15000);
}
