from math import *

n = int(input()) 
dem = 0 
for i in range (2,int(sqrt(n))+1) : dem+=1
print (dem)