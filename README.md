# DHT 11 Temperature and Humidity Data Logger

Author: Bikas Sunar

Project : Thesis

Language : Python and Arduino C++

# Project discription
This project is for collecting real-time tempreature and humidity data from DHT 11 sensor using arduino mega2560.  the arduino sends the data from serial communication and the python script running on a pc,
logs the data into csv files with current date and time. Each data is collected with the frequency of 10s time period.

# files in the project
1)" dhtSensorCode.ino "
  Arduino code does:
  - reads humidity and tempreature from DHT11 sensor
  - sends the data via serial communication
  - outputs data every 10 second

2) " env_mont.py"
   Python code does:
   - Reads serial data from COM3 (port can be changed, depending on the port arduino is connected).
   - adds date and time
   - stores data into csv files.

# Hardware requirements
- Arduino mega2560
- DHT11 sensor
- PC/Laptop

# software requirement
  -- for arduino --
- Arduino IDE
- DHT sensor library by Adafruit
# need to install library
    1. Open Arduino IDE  
    2. Go to **Sketch → Include Library → Manage Libraries**  
    3. Search for: `DHT sensor library`  
    4. Install:
     - **DHT sensor library (Adafruit)**
     - **Adafruit Unified Sensor** (dependency)

  --for python -- 
    - Python 3
    - addition python library (pyserial)
  # need to install pyserial
    pip install pyserial
  
