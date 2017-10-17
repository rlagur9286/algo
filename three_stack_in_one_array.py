# ---------------------------------------------------------
# 하나의 배열을 사용해 세 개의 스택 구현
# 참조: https://www.youtube.com/watch?v=dvL8pkjlxTU&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=12


class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack = [None] * stack_size * 3

        self.stack1_index = 0
        self.stack1_bottom = 0
        self.stack1_top = self.stack1_bottom + self.stack_size

        self.stack2_index = self.stack1_top
        self.stack2_bottom = self.stack1_top
        self.stack2_top = self.stack2_bottom + self.stack_size

        self.stack3_index = self.stack2_top
        self.stack3_bottom = self.stack2_top
        self.stack3_top = self.stack3_bottom + self.stack_size

    def push(self, num, item):
        if num not in [1, 2, 3]:
            print("stack은 1, 2, 3 중에 하나 입니다.")
            return False

        if num == 1:
            if self.stack1_index >= self.stack1_top:
                print("Stack1 Overflow 입니다. 삐-")
                return False
            else:
                self.stack[self.stack1_index] = item
                self.stack1_index += 1
        elif num == 2:
            if self.stack2_index >= self.stack2_top:
                print("Stack2 Overflow 입니다. 삐-")
                return False
            else:
                self.stack[self.stack2_index] = item
                self.stack2_index += 1
        else:
            if self.stack3_index >= self.stack3_top:
                print("Stack3 Overflow 입니다. 삐-")
                return False
            else:
                self.stack[self.stack3_index] = item
                self.stack3_index += 1

    def pop(self, num):
        if num not in [1, 2, 3]:
            print("stack은 1, 2, 3 중에 하나 입니다.")
            return False
        if num == 1:
            if self.stack1_index <= self.stack1_bottom:
                print("Stack1 Underflow 입니다. 삐-")
                return False
            else:
                pop_item = self.stack[self.stack1_index]
                self.stack[self.stack1_index] = None
                self.stack1_index -= 1
                print("Stack1에서 {}을 POP!!!".format(pop_item))
                return pop_item
        elif num == 2:
            if self.stack2_index <= self.stack2_bottom:
                print("Stack2 Underflow 입니다. 삐-")
                return False
            else:
                pop_item = self.stack[self.stack2_index]
                self.stack[self.stack2_index] = None
                self.stack2_index -= 1
                print("Stack1에서 {}을 POP!!!".format(pop_item))
        else:
            if self.stack3_index <= self.stack3_bottom:
                print("Stack3 Underflow 입니다. 삐-")
                return False
            else:
                pop_item = self.stack[self.stack3_index]
                self.stack[self.stack3_index] = None
                self.stack3_index -= 1
                print("Stack1에서 {}을 POP!!!".format(pop_item))

if __name__ == '__main__':
    import random
    st1 = Stack(3)
    st1.push(1, random.randint(0, 1000))
    st1.push(1, random.randint(0, 1000))
    st1.push(1, random.randint(0, 1000))
    st1.push(2, random.randint(0, 1000))
    st1.push(2, random.randint(0, 1000))
    st1.push(0, random.randint(0, 1000))
    st1.push(2, random.randint(0, 1000))
    st1.push(3, random.randint(0, 1000))
    st1.push(3, random.randint(0, 1000))
    st1.push(3, random.randint(0, 1000))
    st1.push(3, random.randint(0, 1000))

    st1.pop(1)
    st1.pop(1)
    st1.pop(1)
    st1.pop(1)