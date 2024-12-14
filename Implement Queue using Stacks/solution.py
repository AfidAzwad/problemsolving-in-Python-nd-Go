class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # rotating the stack to move the newly added element to bottom/index 0
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.pop(0))

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
param_3 = obj.peek()
print(param_3)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()