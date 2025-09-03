class MyQueue:

    def __init__(self):
        self.stack= []   # for push operations
        self.output = []
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()
    def peek(self) -> int:
        if not self.output:  # Transfer elements if output stack is empty
            while self.stack:
                self.output.append(self.stack.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.stack)==0 and len(self.output)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()