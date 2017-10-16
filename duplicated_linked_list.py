# ---------------------------------------------------------
# 링크드리스트에서 중복 문자 제거하기
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)
# 참조: https://www.youtube.com/watch?v=FEYl8kotwts&index=5&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq


class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def show(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
        print('=============================')

    def delete_duplicated_node(self):
        cur = self.head
        prev = None
        dict = {}

        while cur is not None:
            if cur.val in dict:
                prev.next = cur.next
            else:
                dict[cur.val] = True
                prev = cur
            cur = cur.next


if __name__ == '__main__':
    import random
    ll = LinkedList(3)
    for i in range(10):
        ll.add(random.randint(0,5))
    ll.show()

    ll.delete_duplicated_node()

    ll.show()