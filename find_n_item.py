# ---------------------------------------------------------
# 링크드리스트에서 끝에서 n번째 값 구하기
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)
# 참조: https://www.youtube.com/watch?v=bngL6LiupIY&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=7


from duplicated_linked_list import LinkedList


class NewLinkedList(LinkedList):
    def get_size(self):
        cnt = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            cnt += 1
        return cnt

    def find_n_item(self, k):
        if k > self.get_size() - 1:
            print('찾으려는 k 가 LinkedList size 보다 큽니다.')
            return False
        cur = self.head
        p1 = cur
        p2 = cur

        for _ in range(k):
            p2 = p2.next

        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next

        print('Answer : ', p1.val)

if __name__ == '__main__':
    n_ll = NewLinkedList(6)
    n_ll.add(1)
    n_ll.add(4)
    n_ll.add(3)
    n_ll.add(2)
    n_ll.add(6)
    n_ll.add(2)
    n_ll.show()

    n_ll.find_n_item(k=6)