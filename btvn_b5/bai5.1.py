A = tuple(map(int , input().split()))
B = tuple(map(str , input().split()))
k = input('nhap ki tu can dem: ')

def dem (A) :
    sum = 0
    for i in A :
        sum += i 
    sum /= len(A) 
    count = 0
    for i in A :
        if i > sum :
            count += 1
    return count 
def chia (A) :
    Ac = tuple(i for i in A if i % 2 == 0)
    Al = tuple(i for i in A if i % 2 != 0)
    return Ac, Al 
def solanxuathien (k , B) :
    return sum(s.count('k') for s in B) 
def tim (B) :
    e = [s for s in B if len(s) >= 5]
    return len(e)
def kethop (A , B) :
    e = [(i,j) for i in A for j in B]
    _e = tuple(e)
    return _e 
print (kethop(A,B))