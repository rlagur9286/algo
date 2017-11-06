class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class BTree:
    def __init__(self):
        self.head = Node(None)
        self.in_order_list = []
        self.pre_order_list = []
        self.post_order_list = []

    def add(self, item):
        if self.head.val is None:
            self.head = Node(item)
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is None:
                cur.left = Node(item)
            else:
                self.__add_node(cur.left, item)
        else:
            if cur.right is None:
                cur.right = Node(item)
            else:
                self.__add_node(cur.right, item)

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        elif cur.val >= item:
            if cur.left is None:
                print('search Fail!!!')
                return False
            else:
                return self.__search_node(cur.left, item)
        else:
            if cur.right is None:
                print('search Fail!!!')
                return False
            else:
                return self.__search_node(cur.right, item)

    def in_order_traverse(self):
        if self.head is not None:
            self.__in_order(self.head)

    def __in_order(self, cur):
        if cur.left is not None:
            self.__in_order(cur.left)

        self.in_order_list.append(cur.val)
        print(cur.val)

        if cur.right is not None:
            self.__in_order(cur.right)

    def pre_order_traverse(self):
        if self.head.val is not None:
            self.__pre_order(self.head)

    def __pre_order(self, cur):
        self.pre_order_list.append(cur.val)
        print(cur.val)
        if cur.left is not None:
            self.__pre_order(cur.left)

        if cur.right is not None:
            self.__pre_order(cur.right)

    def post_order_traverse(self):
        if self.head is not None:
            self.__post_order(self.head)

    def __post_order(self, cur):
        if cur.left is not None:
            self.__post_order(cur.left)

        if cur.right is not None:
            self.__post_order(cur.right)

        self.post_order_list.append(cur.val)
        print(cur.val)

    def remove(self, item):
        if self.head.val is None:
            print('there is no item')
            return False

        # head가 원하는 값일 때
        if self.head.val == item:
            pass
        # head가 원하는 값이 아닐 때
        else:
            if self.head.val >= item:
                self.__remove(self.head, self.head.left, item)
            else:
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        if cur is None:
            print('there is no item')
            return False
        if cur.val == item:
            # 자식이 없는 자식 일 때
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None

            # 왼쪽 자식만 있을 때
            elif cur.left is not None and cur.right is None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.right

            # 오른쪽 자식만 있을 때
            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right

            # 양 쪽 자식이 다 있는 경우
            else:
                cur.val = self.__most_left_val_from_right_node(cur.right).val
                self.__remove_item(cur, cur.right, cur.val)

    def __most_left_val_from_right_node(self, cur):
        if cur.left is not None:
            return self.__most_left_val_from_right_node(cur.left)
        else:
            return cur

    def __remove_item(self, parent, cur, item):
        if cur.val == item:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur.val > item:
                self.__remove_item(cur, cur.left, item)
            else:
                self.__remove_item(cur, cur.right, item)

if __name__ == '__main__':
    b_tree = BTree()
    b_tree.add(5)
    b_tree.add(3)
    b_tree.add(7)
    b_tree.add(1)
    b_tree.add(4)

    b_tree.in_order_traverse()
    print('')
    b_tree.pre_order_traverse()
    print('')
    b_tree.post_order_traverse()

    print(b_tree.search(3))

    b_tree.remove(3)
    print(b_tree.search(3))
