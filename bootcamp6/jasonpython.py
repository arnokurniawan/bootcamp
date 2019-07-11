import json 

x = '{"name" :"jhon","age": 30,"city": :"new york"} '

#parse x :

y = json.loads(x)
print(y["age"])