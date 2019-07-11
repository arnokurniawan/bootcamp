import re

str = "The  23 Rain in spain falls 45 mainly in the plain"

x = re.findall("[0-5][0-9]",str)
print(x)

if (x):
	print("yes,there is at least one match")
else:
	print("no match")	