def print_factors(x):
	print("faktor dari bilangan ",x,"adalah :")
	for i in range(1,x+1):
		if x % i==0:
			print(i)
angka = int (input("masukan angka :"))
print_factors(angka)		