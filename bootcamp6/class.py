class Hero:
	pass


hero1 = hero() 
hero2 = hero()
hero3 = hero()

hero1.name = "Spiderman"
hero1.health = 200

hero2.name ="batman"
hero2.health = 100

hero3.name = "panji"
hero3.health = 1000

print(hero1)	
print(hero1._dict_)
print(hero1.name)