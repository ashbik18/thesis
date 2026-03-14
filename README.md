# DHT 11 Temperature and Humidity Data Logger

Author: Bikas Sunar

Project : Thesis

Language : Python and Arduino C++

# Project discription
This project is for collecting real-time temperature and humidity data from DHT 11 sensor using arduino mega2560.  the arduino sends the data from serial communication and the python script running on a pc,
logs the data into csv files with current date and time. Each data is collected with the frequency of 10s time period.

# files in the project
1)" dhtSensorCode.ino "
  Arduino code does:
  - reads humidity and temperature from DHT11 sensor
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

## Dataset

The `data/` folder contains temperature and humidity measurements
collected using the DHT11 sensor as part of the environmental monitoring system.

where as export and merged_data can be used for the data analysis


### Sensor Information
- Sensor model: DHT11
- Measured variables: Temperature and Relative Humidity
- Temperature unit: °C
- Humidity unit: %
- Measurement environment: outdoor (Prague)

### Sampling Details
- Sampling interval: 10 seconds
- Data format: CSV
- Timestamp: Recorded at the time of measurement

### File Description
Each CSV file represents an individual measurement session recorded by the
system. The files contain time-series data used for analysis and visualization
in this thesis.

### Reproducibility
The raw data can be reproduced by running the Arduino and Python scripts
provided in this repository.
  
