#! usr/bin/env python3
import time			# To get time for stuff
#import Adafruit_ADS1x115 	# Library for ADS1115 ADC module github.com/adafruit/Adafruit_PythonADS1x15
# variables
repeatLoop = 1
ticks = 0
NumSensorsInUse = 8		# Number of sensors in use

# This determines if the sensor is used or not
SensorUse = [1,1,1,1,0,0,0,0]

# Sets the sensor type
SensorType = ['MAP', 'TEMP', 'MAP', 'TEMP', 'NIL', 'NIL', 'NIL', 'NIL']

# Stores the read value of the sensor
SensorVal = [0,0,0,0,0,0,0,0]

# Sensor Types
"""
MAP
TEMP
AF
ANY5V
NIL
"""

# Setup

# Create ADS1115 instance
#adc = Adafruit_ADS1x15.ADS1115()

# Set the gain for the required voltage range (see ADS1115 data sheet)
# - 2/3 = +/-6.144V
# -   1 = +/-4.096V
# -   2 = +/-2.048V
# -   4 = +/-1.024V
# -   8 = +/-0.512V
# -  16 = +/-0.256V
GAIN = 1

# sensor setup



# Main program loop
while repeatLoop == 1:

	# program code goes here
	print ("Loop number: " + str(ticks) ) 

	# Read sensors
	for i in range(NumSensorsInUse):
		#SensorVal[i] = adc.read_adc(i, gain=GAIN)
		# For DEBUG
		#print("i is " + str(i))
		SensorVal[i] = (i + 69)
		#print('SensorVal[{}] is {}'.format(str(i), str(SensorVal[i])))

	print('Sensor:  1  |   2  |   3  |   4  |   5  |   6  |   7  |')
	print('Value:  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(str(SensorVal[0]),str(SensorVal[1]), str(SensorVal[2]), str(SensorVal[3]), str(SensorVal[4]), str(SensorVal[5]), str(SensorVal[6]), str(SensorVal[7])))

	# Loop Breaker
	if ticks >= 1000:
		break		

	ticks += 1


print ("End Program")
