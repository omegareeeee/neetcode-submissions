class MinStack:
    def __init__(self):
        self.curMin = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.curMin[-1] if self.curMin else val)
        self.curMin.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.curMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curMin[-1]
        
