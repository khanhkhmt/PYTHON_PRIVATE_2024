m = int(input())
ten = []
kl = []
for i in range (m) :
    t = input() 
    ten.append(t)
for i in range (m) :
    k = float(input())
    kl.append(k)
print ('{')
for i in range (m) :
    print ('(' , '"' , ten[i] , '"' , ',' , kl[i] , ')')
print ('}')
total_food = 0
for i in range (m) :
    if (kl[i] < 5) : total_food += 0 
    else : total_food += kl[i] 
    if kl[i] > 100 : break
print (total_food) 
for i in range (m) :
    if kl[i] == max(kl) :
        print(ten[i])
for i in range (m) :
    if kl[i] < 5 : 
        if kl[i] == min (kl) : print (i)
l = []
for i in range (m) :
    if (kl[i] < 5) : l.append(kl[i])
if (len(l) == 0 ) : print ('không có')