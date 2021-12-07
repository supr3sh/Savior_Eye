import serial
import time
import string
import pynmea2
from geopy.geocoders import Nominatim

# while True:
    # port="/dev/ttyAMA0"
    # ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    # dataout = pynmea2.NMEAStreamReader()
    # newdata=ser.readline()

    # if newdata[0:6] == "$GPRMC":
        # newmsg=pynmea2.parse(newdata)
        # lat=newmsg.latitude
        # lng=newmsg.longitude
		# locator = Nominatim(user_agent="myGeocoder")
		# coordinates = "53.480837, -2.244914"
		# location = locator.reverse(coordinates)
		# location.raw
        # #gps = str(lat)+ "," + str(lng)
        # #print(gps)
    
lat_arr = []
long_arr = []    
#while len(lat_arr)!=5:
#	port="/dev/ttyAMA0"
#	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
#	dataout=pynmea2.NMEAStreamReader()
#	newData = ser.readline()
#	
#	if newData[0:6]=="$GPRMC":
#		msg=pynmea2.parse(newData)
#		lat_arr.append(msg.latitude)
#		long_arr.append(msg.longitude)

#avg_lat=sum(lat_arr)/len(lat_arr)
#	avg_long=sum(long_arr)/len(long_arr)

locator=Nominatim(user_agent="myGeocoder")
coordinates="32.66698,74.8588075"
location=locator.reverse(coordinates)
print(location.address)
