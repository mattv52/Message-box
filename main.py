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
		# Reset Button

		# Send to boltB

		# Activate LED Notification for boltA (Message sent)

		# Activate LED Notification for boltB (Message waiting)
	# else message waiting
		# Reset Button

		# Update LED Notification for boltB (Message recieved)

		# Update LED Notificaion for boltA (Message read)

		# Wait some time then remove message

else:
	time.sleep(READ_RATE)