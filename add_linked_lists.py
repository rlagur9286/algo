# ---------------------------------------------------------
# 링크드리스트로 표현된 두 수의 합을 반환하는 알고리즘
# 참조: https://www.youtube.com/watch?v=jOSSTTYw2sg&index=10&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq
from duplicated_linked_list import LinkedList


def add_linked_lists(list1, list2):
    carry = 1
    r1, r2 = 0, 0
    l1 = list1.get_head()
    while l1 is not None:
        r1 += (carry * l1.val)
        carry *= 10
        l1 = l1.next

    carry = 1
    l2 = list2.get_head()
    while l2 is not None:
        r2 += (carry * l2.val)
        carry *= 10
        l2 = l2.next

    return r1 + r2

if __name__ == '__main__':
    l_list1 = LinkedList(7)
    l_list1.add(1)
    l_list1.add(6)
    l_list1.add(4)

    l_list2 = LinkedList(5)
    l_list2.add(9)
    l_list2.add(2)

    result = add_linked_lists(l_list1, l_list2)
    print(result)