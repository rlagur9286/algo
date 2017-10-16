# ---------------------------------------------------------
# 링크드리스트에서 중간 노드 삭제하기
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)
# 참조: https://www.youtube.com/watch?v=_RUGwY_tCFE&index=8&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq

from duplicated_linked_list import LinkedList


class NewLinkedList(LinkedList):
    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur is not None:
                if cur.val == item:
                    self.removeFromList(item)
                    return
                cur = cur.next
            print('찾으려는 item을 발견하지 못하였습니다.')

    def removeFromList(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                next_node = cur.next.next
                cur.next.next = None
                cur.next = next_node
                break
            cur = cur.next


if __name__ == '__main__':
    n_ll = NewLinkedList(6)
    n_ll.add(1)
    n_ll.add(4)
    n_ll.add(3)
    n_ll.add(2)
    n_ll.add(6)
    n_ll.add(2)
    n_ll.show()

    n_ll.remove(2)
    n_ll.show()