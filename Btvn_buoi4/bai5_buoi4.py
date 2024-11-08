n = int(input()) 
list = [int(input()) for i in range (n)] 
x = int(input('nhap so can tim: '))
l = 0 
r = len(list) - 1
kt = False
while l < r :
    m = (l+r) // 2
    if x == list[m] :
        print (m+1) 
        kt = True
        break 
    if (x > list[m]) :
        l = m + 1
    else :
        r = m - 1 
if kt == False : print(-1)