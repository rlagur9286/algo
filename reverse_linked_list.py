# ---------------------------------------------------------
# Palindrome in Linkedlist (링크드리스트에서 회문 구하기)
# 참조: https://www.youtube.com/watch?v=eU0fIKv3R-c&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=11

from duplicated_linked_list import LinkedList


def check_palindrome(linked_list):
    cur = linked_list.get_head()
    prev = None
    next = None

    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    linked_list.head = prev

if __name__ == '__main__':
    ll = LinkedList(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)

    check_palindrome(ll)
    ll.show()