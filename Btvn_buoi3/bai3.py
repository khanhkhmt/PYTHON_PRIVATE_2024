n = int(input()) 
name = []
diem_l1 = []
diem_l2 = []
tong = []
loai = []
for i in range (n) :
    na = input()
    name.append(na)
    diem1 = int(input())
    diem_l1.append(diem1) 
    diem2 = int(input())
    diem_l2.append(diem2) 
    sum = diem_l1[i] + diem_l2[i]
    tong.append(sum) 
    if (tong[i] >= 190) : loai.append('xuất sắc')
    elif tong[i] >= 150 and tong[i] < 190 : loai.append('giỏi')
    elif tong[i] >= 100 and tong[i] < 150 : loai.append('khá')
    else : loai.append('yếu')
kq = zip (name , tong , loai)
for index , (i,j,k) in enumerate (kq) :
    print (index+1 , i ,j ,k)