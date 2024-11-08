list1 = list(map(int , input().split()))
list2 = list(map(int , input().split()))
kq = []
for i in list1[::-1] :
    if i in list2 : 
        kq.append(i) 
        list1.remove(i)
print (kq)