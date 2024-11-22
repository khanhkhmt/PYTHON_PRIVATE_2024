def f (n) :
    f = 1 
    for i in range (1,n+1) :
        f *= i 
    return f 
def tinh (x) : 
    n = 1000
    e = 1
    for i in range (1,n+1) :
        e += (x ** i) / f(i)
    return e
x = int(input())
print ('e^x = ' , tinh(x))