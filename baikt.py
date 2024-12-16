class Stack :
    '''
    Lớp đại diện cho cấu trúc dữ liệu ngăn xếp (stack).

    Thuộc tính:
    
    capacity : int
        Sức chứa tối đa của ngăn xếp (số phần tử tối đa có thể lưu trữ).
    st : list
        Danh sách lưu trữ các phần tử trong ngăn xếp.

    Phương thức:
    
    isEmpty() -> bool:
        Kiểm tra xem ngăn xếp có rỗng hay không.
    isFull() -> bool:
        Kiểm tra xem ngăn xếp đã đầy hay chưa.
    pop():
        Loại bỏ và trả về phần tử trên cùng của ngăn xếp. Trả về `False` nếu ngăn xếp rỗng.
    push(value):
        Thêm một phần tử vào ngăn xếp. In thông báo nếu ngăn xếp đã đầy.
    top():
        Trả về phần tử trên cùng của ngăn xếp mà không loại bỏ. Trả về `False` nếu ngăn xếp rỗng.
    '''
    def __init__(self , capacity : int):
        self.capacity = capacity 
        self.st = []
    def isEmpty(self) -> bool : 
        return len(self.st) == 0
    def isFull(self) -> bool :
        return  len(self.st) >= self.capacity
    def pop(self) :
        if self.isEmpty() :
            return None
        else :
            p = self.st.pop() 
            return p
    def push(self, value : int) :
        if self.isFull() : print ("stack is full")
        else:
            return self.st.append(value) 
    def top (self) :
        if self.isEmpty():
            return None
        else:
            top_value = self.st[-1]
            return top_value

stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())