n = int(input('nhập n: ')) 
x = int(input('nhập x: '))
def gt (t) :
    f = 1
    for i in range (1 ,t+1) :
        f *= i 
    return f 
kq = 1 
for i in  range (1 , n+1) :
    kq += (x ** i) / gt(i) 
print (kq) 
kq1 = 0 
for i in range (1 ,n+1) :
    kq1 += 1 / gt (i) 
print (kq1) 
