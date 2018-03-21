#! usr/bin/env python3
import time			# To get time for stuff
#import Adafruit_ADS1x115 	# Library for ADS1115 ADC module
# variables
repeatLoop = 1
ticks = 0

# This determines if the sensor is used or not
SensorUse = [1,1,1,1,0,0,0,0]

# Sets the sensor type
SensorType = ['MAP', 'TEMP', 'MAP', 'TEMP', 'NIL', 'NIL', 'NIL', 'NIL']

# Stores the read value of the sensor
SensorVal = []

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


# Start the ADC
#adc.start_adc(0, gain=GAIN)

# Main program loop
while repeatLoop == 1:

	# program code goes here
	print ("Loop number: " + str(cnt) ) 

	# Loop Breaker
	if ticks >= 10:
		break		

	cnt += 1

# stop the ADC
#adc.stop_adc()

print ("End Program")
