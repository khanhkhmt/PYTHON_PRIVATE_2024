s= input() 
print (len(s))
vt = int ((len(s) -1) / 2 ) -1
print (s[vt])
kq = 1
for i in range (vt ,len(s)) :
    if s[vt] == '@' or s[i] == '.' :
        kq = 1
    else : kq = 0
if kq == 1 :
    print ('Valid')
else : print ('Invalid')