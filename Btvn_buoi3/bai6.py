import math
def is_number (x) :
    try :
        float (x) 
        return True 
    except ValueError :
        return False 
def activation_function_name (s) :
    return s in ('binary' , 'sigmoid' , 'elu') 
def Binary (x) :
    if x < 0 :
        return 0
    else :
        return 1
def Sigmoid (x) :
    return 1 / (1 + (math.e ** (-x)))
def ELU (x , alpha) :
    if x < 0 :
        return alpha * (math.e ** x - 1)
    else :
        return x 
x = input()
activation_function = input() 
alpha = float(input())
if (is_number(x)) :
    x = float(x) 
    if (activation_function_name(activation_function)) :
        if activation_function == 'binary' : print (Binary(x))
        if activation_function == 'sigmoid' : print(Sigmoid(x)) 
        if activation_function == 'elu' : print(ELU(x,alpha)) 
    else : print (activation_function , 'is not supported')
else : print ('x must be number')