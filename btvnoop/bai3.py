class MyStack :
    def __init__(self , capacity):
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
    def push(self, value) :
        if self.isFull : print ("stack is full")
        else:
            self.st.append(value) 
    def top (self) :
        if self.isEmpty():
            return None
        else:
            top_value = self.stack[-1]
            return top_value
stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())

print(stack1.top())

print(stack1.pop())

print(stack1.top())
