s = input() 

kq = ''
s = list(s)
for i in range (len(s)) :
    if s[i] == '[' :
        b = i + 1
        n = int (s[i-1])
    if s[i] == ']' :
        e = i -1 
    kq += ''.join(s[b : e+1]) * n
print (kq)