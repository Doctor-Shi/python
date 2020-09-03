import json

data = ['aa', 'bb', 'cc']
str2 = json.dumps(data)
print(str2)
str1 = json.loads(str2)
print(str1)


list1 = ['google', 'runoob',]