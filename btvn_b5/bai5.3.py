def swap (dict1) :
    dict2 = {}
    for key , value in dict1.items() :
        if value in dict2 :
            return None 
        dict2[value] = key
    return dict2 
dict1 = {'name': 'Alice', 'age': 26, 'city': 'hanoi', 'country': 'vietnam', 'company': 'FPT' , 1 : "FPT"}
print (swap(dict1))