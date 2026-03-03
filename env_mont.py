import serial
import csv
from datetime import datetime

ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)

with open('dht11_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Time", "Humidity(%)", "Temperature(C)"])

    while True:
        line = ser.readline().decode('utf-8').strip()

        if not line:
            continue

        humidity, temperature = line.split(',')

        now = datetime.now()

        writer.writerow([
            now.date(),
            now.strftime("%H:%M:%S"),
            humidity,
            temperature
        ])

        file.flush()

        print(now, humidity, temperature)
