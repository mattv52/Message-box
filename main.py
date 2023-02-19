from boltiot import Bolt
from conf import API_KEY
import time, json

READ_RATE = 60
DEVICE_A = "BOLT5036298"
boltA = Bolt(API_KEY, DEVICE_A)
# DEVICE_B = ""
# boltB = Bolt(API_KEY, DEVICE_B)

res = boltA.digitalRead('0')
if res.value == "1":
	# Button has been pressed
	# if no message waiting
		# Send mesasage to boltB

	# else message waiting
		# Start timer to remove message
	
	# Reset Button

else:
	time.sleep(READ_RATE)
