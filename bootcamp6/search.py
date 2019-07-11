import re

str = "The  23 Rain in spain falls 45 mainly in the plain"

x = re.search("\s",str)


print("The first white-space charcter is located position:",x.start())