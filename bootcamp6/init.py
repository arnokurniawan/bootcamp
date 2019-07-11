"""class Person:
	def __init__(self,name,alamat,umur):
		self.name = name
		self.adress = alamat
		self.age = umur

	def say_hi(self):
		print("hello,myname is {} my adress {} my age {} ".format(self.name,self.adress,self.age) )

p = Person('swaroop','mampang',29)
p.say_hi()
p.name = 'wiro'
p.adress = 'bangka'
del.p.name()
p.say_hi()
p2 = Person('Ali','Bandung',25)
p2.say_hi()	
"""
class Robot:

	population =0

	def __init__(self,name):
		self.name = name
		print("Initialiazing{}".format(self.name))
		
		Robot.population += 1

	def die(self):
		print("{} is being destroyed".format(self.name))

		Robot.population -=1

		if Robot.population == 0:
			print("{} was the last one".format(self.name))
		else:
			print("there are still {:d} robots is working.".format(Robot.population))

	def say_hi(self):
			print("greting,my master call me{}.".format(self.name))

	@classmethod
	def how_many(cls):		
 			print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

droid3 = Robot("CR-7")
droid3.say_hi()
Robot.how_many()


print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
