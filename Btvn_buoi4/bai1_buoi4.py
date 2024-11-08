k = int(input('nhap k: ')) 
a = [int(input()) for i in range(k)] 
n = int(input('nhap n: '))
m = int(input('nhap m: ')) 
if n * m <= k :  
    mt = [a[i * m : (i+1) * m] for i in range (n)] 
    print (mt) 
else : print ("khong tao duoc ma tran")