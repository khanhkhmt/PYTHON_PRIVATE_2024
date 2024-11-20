dict1 = {input() : input() for i in range(8)}
dict1["version"] = '3.10' 
print (dict1)
print (dict1["image"])
dict1["environment"] = 'PYTHONUNBUFFERED=1'
if 'volumes' in dict1 :
    print('yes')
else : print('no')
del dict1['depends_on '] 
print (dict1)
print(len(dict1))
ds = []
for value in dict1.values() :
    ds.append(value)
print (ds)
# version 
# '3.8'
# services
# app
# image
# python:3.10-slim
# command
# python app.py
# volumes
# ./app:/app
# restart 
# always
# ports
# 5000:5000
# depends_on 
# db