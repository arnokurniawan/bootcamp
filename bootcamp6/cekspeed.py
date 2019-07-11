def checkSpeed(speed):
 	if speed < 70:
 		return 'ok'
 	elif speed > 70:
 		point = (speed-70) / 5
 		print(f'Points: {point}')
 		if point > 12:
 			print('License suspended')
