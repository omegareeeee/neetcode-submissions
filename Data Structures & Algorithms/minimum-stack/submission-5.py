class MinStack:

    def __init__(self):
        self.stk = []
        self.mins = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)

        if  len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)
        

    def pop(self) -> None:
        if self.top() == self.mins[-1]:
            self.mins.pop()
        self.stk.pop()

        

    def top(self) -> int:
        return self.stk[-1] if self.stk else -1
        

    def getMin(self) -> int:
        return self.mins[-1] if self.stk else -1
        
