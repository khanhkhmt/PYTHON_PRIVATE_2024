ds_dang_ki = set(map(str , input().split()))

ds_da_check_in = set(map(str , input().split()))

ds = [b for b in ds_dang_ki if b not in ds_da_check_in]
print ('danh sach cac bn chua check in: ' , ds)
d1 = [b for b in ds_da_check_in if b in ds_dang_ki] 
d2 = [b for b in ds_da_check_in if b not in ds_dang_ki]
print ('tong so luong cac bn da dang ki va check_in' ,len(d1) + len(d2))
ds_dang_ki = sorted (ds_dang_ki) 
print (ds_dang_ki) 