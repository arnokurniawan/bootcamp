import modul
modul.greeting("elga P")

from modul import person

a = modul.person["age"]
print(a)

"""for x in (modul.person):
	print (x,modul.person[x])
"""
for x,y in modul.person.items():
	print(x,y)	

