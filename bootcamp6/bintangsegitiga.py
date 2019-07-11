string = ""
baris = 1

x =int(input("masukan angka :"))

#looping baris
while baris <= x:
	kolom = baris

	#looping kolom
	while kolom > 0:
		string = string + "*"
		kolom = kolom - 1

	string = string + "\n"
	baris = baris + 1

	print(string)
