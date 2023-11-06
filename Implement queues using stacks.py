class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        
        #stack1 =[1,2,3]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        #stack2=[3,2,1]
        ans=self.stack2.pop()
        #stack2=[3,2]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            #stack1=[2,3]
        return ans
        
        
    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            #stack2=[3,2]

        res= self.stack2[-1] #the top is 2
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            #stack1=[2,3]
        return res

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
