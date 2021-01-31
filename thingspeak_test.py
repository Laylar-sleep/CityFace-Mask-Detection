import serial
import time
import thingspeak
channel_id = 1292897
write_key = 'B08G531MODNBAC7C'
a=0
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM9'
ser.open()
channel=thingspeak.Channel(id=channel_id,api_key=write_key)
while 'true':
    a=ser.readline();
    time.sleep(0.1)
    print(a)
    response = channel.update({1:99})
    time.sleep(0.090)
