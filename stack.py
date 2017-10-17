# ---------------------------------------------------------
# Stack 구현


class Stack:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) == self.max_size:
            print("Stack Overflow")
        else:
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack Underflow")

    def print_list(self):
        print(self.items)

    def peak(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(5)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
