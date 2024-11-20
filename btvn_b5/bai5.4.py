import random 

def create_account (n) :
    password = ['CNTT' , 'KHMT' , 'KTPM' , 'HTTT' , 'DAPT'] 
    
    accounts = {}
    
    for i in range (1 , n + 1) :
        
        id = f"{2023600000+i}" 
        
        random_password = random.choice(password) 
        main_password = f"{random_password}{id}"
        
        accounts[f"acount{i}"] = {
            "username" : id , 
            "password" : main_password
        }
    return accounts
n = int(input('nhap so tai khoan: ')) 
for key , value in create_account(n).items() :
    print (f"{key} : {value}")