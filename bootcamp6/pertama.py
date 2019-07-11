"""
print("hello word")

a= 1
b= 2
c= a+b
print(c)

if 5 > 2:
	print("five is greater than two")

x = " awasome "
print("python is" + x)

x=1	# int
y=2.8 # float
z=1j # complex

print(type(x))
print(type(y))
print(type(z))

x=1 #int
y=2.8 # float
z=1j # complex

#convert from int to float :
a = float(x)

#convert from float to int :
b= int(y)

#convert from to complex :
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x= int(1) # x will be 1
y= int(2.8) # y will be 2
z= int ("3") # z will be 3
w=float("4.2") # will be 4.2

x=str("S1") # will be 1.0
y=str(2)
z=str(3.0)




a ="2 orang"
print([a])

a=" hello, world!"
print(a.strip())
print(a.lower())
print(a.upper())
print(a.split("w"))

age = 26
txt = "my name is john,and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {} dollar for{} prices or item {}"
print(myorder.format(quantity, itemno, price))

x= ["apple","banana"]
print("pisang" not in x)
print("apple" in x)
#menggunkan thislist
thislist = ["apple","banana","melon","buah naga"]
print(thislist)
print(thislist[1])
thislist[1]="rambutan"
print(thislist)
print(len(thislist))
#menggunakan tuples
thistuples = ("apple","banana","melon","buah naga")
print(thistuples)
print(thistuples[2])
#for x in thistuples :
	#print(x)

	#change value
thisset = {"apple","banana","melon","buah naga"}
print(thisset)
thisset.add("semangka")

for x in thisset :
	print(x)

thisdict = {"brand" : "Ford","model" : "Mustang","year" : "1964"}
print(thisdict)
#kondisi if else

a = 33
b = 200
if b > a:
	print("b lebih besar dari a")
elif a == b:
	print("a dan b adalah sama")



i = 1
while i < 6:
	print(i)
	i +=1

fruits = "banana","apel","nanas"
for x in fruits :

	print(x)
#loops
adj = ("1", "2", "3")
fruits = ("apple", "banana", "cherry")

for x in adj:
  for y in fruits:
    print(x, y)
    

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
for x in range(6):
  print(x) 

for x in range(2, 30, 3):
  print(x) 

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("kabayan")
my_function("ateng")
my_function("acong")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

def my_function():
	print("Hello from a function")
 
my_function() 


print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function(x):
  return 5 * x
"""
def myfunc(n):
  return lambda z : z + n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
