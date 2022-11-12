def __init__(self):
    self.stack = []
    

def push(self, x: int) -> None:
    self.stack.insert(0,x)
    

def pop(self) -> int:
    r = self.stack[0]
    self.stack.pop(0)
    return r
    

def top(self) -> int:
    return self.stack[0]
    

def empty(self) -> bool:
    if not self.stack:
        return True
