class Stack:
    def __init__(self):
        self.stack = []
    def push(self,value): #adds an element to the top of the stack
        self.stack.append(value)
    def pop(self): #removes the top element of the stack
        if len(self.stack) ==0:
            return "Stack is empty"
        return self.stack.pop()
    def peek(self): #returns the top element of the stack
        if len(self.stack) ==0:
            return "Stack is empty"
        return self.stack[-1]
    def size(self): #returns the size of the stack
        return len(self.stack)
    def is_empty(self): #returns True if the stack is empty, False otherwise
        if len(self.stack) ==0:
            return True
        return False
    def is_full(self): #returns True if the stack is full, False otherwise

        return False #stack is never full in python because of the dynamic nature of the list
    def __str__(self): #returns the elements of the stack
        return str(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack.is_full())


#5,4,1,2,3




# time complexity of the operations is O(1) because we are using a list to implement the stack but for __str__ it is O(n) where n is the size of the stack