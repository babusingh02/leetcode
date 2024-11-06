class MinStack:

    def __init__(self):
        self.stack=[]
        self.mn=0
        

    def push(self, val: int) -> None:
        if self.stack:
            self.mn=min(self.stack[-1][0],val)
        else:
            self.mn=val
        self.stack.append([self.mn,val])
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][1]
        

    def getMin(self) -> int:
        return self.stack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()