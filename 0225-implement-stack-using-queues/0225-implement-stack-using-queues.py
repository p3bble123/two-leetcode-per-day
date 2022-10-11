class MyStack:

    def __init__(self):
        self.val = []

    def push(self, x: int) -> None:
        self.val.append(x)

    def pop(self) -> int:
        return self.val.pop(-1)

    def top(self) -> int:
        return self.val[-1]

    def empty(self) -> bool:
        if len(self.val) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()