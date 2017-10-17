# ---------------------------------------------------------
# 2개의 스택을 사용하여 큐를 구현하라
# 참조: https://www.youtube.com/watch?v=4u2ON2hwjSA&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=15

from stack import Stack


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
