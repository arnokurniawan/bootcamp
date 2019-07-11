class Hero:
	pass


hero1 = Hero() 
hero2 = Hero()
hero3 = Hero()

hero1.name = "Spiderman"
hero1.health = 200

hero2.name ="batman"
hero2.health = 100

hero3.name = "panji"
hero3.health = 1000

print(hero1)	
print(hero1.__dict__)
print(hero1.name)