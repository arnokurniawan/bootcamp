class inputanString:
	def __init__(self):
		self.a = ""
	def getString(self):
		self.a = input("masukan kata :")
	def printString(self):
		print(self.a.upper())	

x = inputanString()
x.getString()
x.printString()
#a= re.findall("[A-Z]",str)

