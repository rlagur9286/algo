# ---------------------------------------------------------
# 스택 시간복잡도 O(1)으로 최소값 구하기
# 참조: https://www.youtube.com/watch?v=9wekIo_yuMg&index=13&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq


class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
        self.min = None

    def push(self, item):
        self.stack.append(item)
        self.mins.append(self.min)
        if self.min is None or self.min > item:
            self.min = item

    def pop(self):
        self.stack.pop()
        self.min = self.mins.pop()

    def get_minimun(self):
        return self.min

    def show(self):
        for item in self.stack:
            print(item)
        print("=============================")

if __name__ == '__main__':
    m_stack = MinStack()

    m_stack.push(1)
    m_stack.push(5)
    m_stack.push(2)
    m_stack.push(0)
    m_stack.show()

    m_stack.pop()
    print(m_stack.get_minimun())