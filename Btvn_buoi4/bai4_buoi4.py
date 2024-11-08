import random 
import math
def random_list (num_sample) :
    y_t = [random.uniform(0,10) for _ in range(num_sample)] 
    y_p = [random.uniform(0,10) for _ in range(num_sample)]
    return y_t , y_p
def is_number (num_sample) :
    try : 
        num_sample = int(num_sample)
        return num_sample > 0
    except :
        return False 
def activation_function_name (s) :
    return s in ('MAE' , 'MSE' , 'RMSE' , 'Huber Loss')
def Mae (y_t , y_p) :
    s = 0 
    for i in range (num_sample) :
        s += abs(y_t[i] - y_p[i])
    return s / num_sample
def Mse (y_t , y_p) :
    s = 0 
    for i in range (num_sample) :
        s += (y_t[i]-y_p[i])**2
    return s / num_sample
def Rmse (y_t , y_p) :
    return Mse(y_t,y_p) ** (1/2)
def Huber_loss (y_t , y_p) :
    s = 0 
    for i in range (num_sample) :
        if abs(y_t[i] - y_p[i]) <= 0.5 :
            s += (1/2) * (y_t[i] - y_p[i]) ** 2
        else :
            s += 0.5 * (abs(y_t[i] - y_p[i]) - 1 /4)
    return s / num_sample
if __name__ == "__main__": 
    num_sample = input ()
    loss_name = input() 
    if (is_number(num_sample)) :
        num_sample = int (num_sample)
        y_t , y_p = random_list (num_sample)
        if activation_function_name (loss_name) :
            if loss_name == 'MAE' : print ("kq la: " , Mae(y_t , y_p))
            if loss_name == 'MSE' : print ("kq la:" , Mse (y_t , y_p)) 
            if loss_name == 'RMSE' : print ("kq la: " , Rmse(y_t , y_p)) 
            if loss_name == 'HUBER_LOSS' : print("kq la: " , Huber_loss(y_t , y_p))
        else : print ("loss name loss is not supported")
    else : print ('number of samples must be a postive integer number')