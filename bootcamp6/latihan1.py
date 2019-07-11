"""
y=input("masukan data : ")

hitung_angka=0
hitung_huruf=0
hitung_simbol=0

for x in y:
	if x.isnumeric()==True:
		hitung_angka = hitung_angka +1
	elif x.isalpha()==True:
		hitung_huruf = hitung_huruf +1
	else:
		hitung_simbol = hitung_simbol +1

print('angka = {}, huruf = {} , simbol = {}'.format(hitung_angka,hitung_huruf,hitung_simbol))	
"""
"""z=input("masukan jumlah :")
print("masukan angka :" +str(z))

i=1

while i<=10:
	print(str(i)+"x"+str(z)+"="+str(i*int(z)))
	i+=1"""


f = input("masukan suhu  : ")
a = input("masukan 1(Celcius-Farenheit),2(Farenheit-Celcius) : ")
if int(a)<=1:
	print("konversi suhu adalah : " + str(((9/5)*int(f)) + 32) + "F")
else:
	print("konversi suhu adalah : " + str((int(f)-32) *(5/9))+ "C")



