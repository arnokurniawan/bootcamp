import re

str=input("masukan kata : ")


a= re.findall("[A-Z]",str)
print(a)