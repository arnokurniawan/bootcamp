

while True:
	try:
		angka =int(input("masukan angka :"))

		if angka > 0 :
			if (angka % 2) == 0 :
				print(angka,'adalah bilangan genap')
			else:
				print(angka,'adalah bilangan ganjil')
				break	
					
	except Exception:
		print("mohon masukan angka")	


				