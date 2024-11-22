s = input()

_s = set(s) 
dem = {}
for i in _s :
    dem[i] = s.count(i) 
print (dem)