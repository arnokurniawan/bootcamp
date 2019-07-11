class Hero:
	#class variable
	jumlah_hero = 0
	def _init_(self,inputName,inputHealth,inputPower,inputArmor):
		#intance variable
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah_hero += 1

		#void function,method tanpa return,tanpa argumen
	def siapa(self):
		print("namaku adalah " + self.name)



hero1 = Hero('sniper',100,10,5)
hero2 = Hero('mario',90,5,10)

hero1.siapa()
hero1.health()	