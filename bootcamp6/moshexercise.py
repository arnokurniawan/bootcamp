'''NUMBER 1'''
 def maximum_number(num1, num2):
 	if num1 > num2:
 		return num1
 	elif num1 < num2:
 		return num2
 	else:
 		return f'{num1} = {num2}'

'''NUMBER 2'''
#
 def fizz_buzz(number):
 	if (number % 3 == 0) and (number % 5 != 0):
 		return 'Fizz'
 	elif (number % 5 == 0) and (number % 3 != 0):
 		return 'Buzz'
 	elif (number % 5 == 0) and (number % 3 == 0):
 		return 'FizzBuzz'
 	else:
 		return number

'''NUMBER 3'''
 def check_speed(speed):
 	if speed < 70:
 		return 'ok'
 	elif speed > 70:
 		point = (speed-70) / 5
 		print(f'Points: {point}')
 		if point > 12:
 			print('License suspended')

'''NUMBER 4'''
 def showNumbers(limit):
 	if limit > 0:
 		for element in range(0, limit):
 			if element % 2 == 0:
 				print(f'{element} EVEN')
 			else:
 				print(f'{element} ODD')
 	if limit < 0:
 		print('you can not input limit by negative number')

'''NUMBER 5'''
 def sumNumber(limit):
 	jumlah = 0
 	for element in range(0, limit+1):
 		if element % 3 == 0 or element % 5 == 0:
 			jumlah += element
 	return jumlah


'''NUMBER 6'''
 def show_stars(rows):
 	i = 1
 	for element in range(1, rows+1):
 		print(i * '*')
 		i += 1

'''NUMBER 7'''
 def primeNumber(limit):
 	for element in range(0,limit+1):
 		if element > 1:
 			for n in range(2, element):
 				if (element % n) == 0:
 					break
 			else:
 				print(element)