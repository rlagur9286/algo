# ---------------------------------------------------------
# 특정 노드를 기준으로 링크드리스트를 나누는 코드
# 참조: https://www.youtube.com/watch?v=NVBL4AebL6k&index=9&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq


from duplicated_linked_list import LinkedList
from duplicated_linked_list import Node


class NewLinkedList(LinkedList):
    def get_head(self):
        return self.head

    def devide_linked_list(self, target):
        cur = self.head
        post = None
        prev = None
        while cur is not None:
            if cur.val == target:
                pass
            else:
                if cur.val < target:
                    if prev is None:
                        prev = NewLinkedList(cur.val)
                    else:
                        prev.add(cur.val)
                else:
                    if post is None:
                        post = NewLinkedList(cur.val)
                    else:
                        post.add(cur.val)
            cur = cur.next
        if prev:
            cur = prev.get_head()
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(target)
        cur.next.next = post.get_head()
        self.head = prev.get_head()

if __name__ == '__main__':
    n_ll = NewLinkedList(6)
    n_ll.add(3)
    n_ll.add(8)
    n_ll.add(1)
    n_ll.add(5)
    n_ll.add(9)

    n_ll.devide_linked_list(5)
    n_ll.show()
