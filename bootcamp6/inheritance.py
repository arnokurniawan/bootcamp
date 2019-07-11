class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname,self.year)

#Use the Person class to create an object, and then execute the printname method:
class Student(Person):	

	def __init__(self,fname,lname,year):
		Person.__init__(self,fname,lname,year)
		self.graduation = year

x = Student("Mike", "Doel",2019)
x.printname()
