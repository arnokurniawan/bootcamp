import re

str = "The rain in Spain"

x1= re.sub("\s","78",str)

x= re.search(r"\bS\w+",str) 
print(x1)
print(x.span())