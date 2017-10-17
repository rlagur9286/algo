# ---------------------------------------------------------
# 스택Set Of Stacks를 구현하라
# 참조: https://www.youtube.com/watch?v=yPLx3kPc4vE&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=14


class InfiniteStack:
    def __init__(self, max_stack_size=3):
        self.stack_list = []
        self.max_stack_size = max_stack_size
        self.stack_list.append([])

    def push(self, item):
        st = self.get_last_stack()
        if len(st) == self.max_stack_size:
            new_st = list()
            new_st.append(item)
            self.stack_list.append(new_st)
        else:
            st.append(item)

    def pop(self):
        st = self.get_last_stack()
        if len(st) == 0:
            self.stack_list.pop()
            st = self.get_last_stack()
            return st.pop()
        else:
            return st.pop()

    def get_all_items(self):
        result = list()
        for stack in self.stack_list:
            for item in stack:
                result.append(item)
            result.append('|')
        return result

    def get_last_stack(self):
        return self.stack_list[-1]

if __name__ == '__main__':
    inf_stack = InfiniteStack()

    inf_stack.push(1)
    inf_stack.push(2)
    inf_stack.push(3)
    inf_stack.push(4)
    inf_stack.push(5)
    inf_stack.push(6)
    inf_stack.push(7)
    inf_stack.push(7)

    inf_stack.pop()
    res = inf_stack.get_all_items()
    print(res)