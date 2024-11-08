n = int(input()) 
m = int(input())
a = [input() for i in range (n)] 
b = [int(input()) for i in range (m)] 
c = []
if n < m :
    for i in range (n) : 
        c.append (a[i])
        c.append (b[i])
    for j in range (n , m) :
        c.append (b[j])
else :
    for i in range (m) :
        c.append (a[i])
        c.append (b[i])
    for j in range (m , n) :
        c.append (a[j])
print (c)