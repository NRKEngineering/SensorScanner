#! usr/bin/env python3

# Main program loop

repeatLoop = 1
cnt = 0

while repeatLoop == 1:

	# program code goes here
	print ("Loop number: " + str(cnt) ) 

	# Loop Breaker
	if cnt >= 10:
		break		

	cnt += 1

print ("End Program")
