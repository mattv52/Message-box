from boltiot import Bolt
from sqlitedict import SqliteDict
from conf import API_KEY, READ_RATE, MESSAGE_TIME, DEVICE_ELYSE, DEVICE_MATT, DATA
import time, json

Bolt = Bolt(API_KEY, DEVICE_MATT)

wait_for_message = False

# pin 0 - reset
# pin 1 - read button
# pin 3 - send message

Bolt.digitalWrite('3', 'LOW')
while True:
	# Read button
	res = json.loads(Bolt.digitalRead('1'))
	print(res)
	with SqliteDict(DATA) as data:
		# if message has been sent, turn on message
		message = data['Elyse_to_Matt']
		if message == True:
			Bolt.digitalWrite('3', 'HIGH')

		# Button has been pressed
		if res['value'] == '1':
			print("ON")
			# if no message waiting
			if message == False:
				# Send message to Elyse
				data['Matt_to_Elyse'] = True
				data.commit()

			# else message waiting
			else:
				# Start timer to remove message
				wait_for_message = True
				data['Elyse_to_Matt'] = False
				data.commit()
			
			# Reset Button
			Bolt.digitalWrite('0', 'HIGH')
			Bolt.digitalWrite('0', 'LOW')
		
		else:
			print("OFF")
	

	# Wait
	if wait_for_message:
		time.sleep(MESSAGE_TIME)
		Bolt.digitalWrite('3', 'LOW')

		wait_for_message = False

	else:
		time.sleep(READ_RATE)

