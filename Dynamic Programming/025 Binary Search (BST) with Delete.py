class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,val):
        if val == self.data:
            return

        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTree(val)

        if val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTree(val)

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        # Visit Left Node
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit Base Node
        elements.append(self.data)

        # Visit Right Node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):

        # Visit Base Node
        elements = [self.data]

        # Visit Left Node
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit Right Node
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):

        elements = []

        # Visit Left Node
        if self.left:
            elements += self.left.post_order_traversal()

        # Visit Right Node
        if self.right:
            elements += self.right.post_order_traversal()

        # Visit Base Node
        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_min()


    def deleteNode(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.deleteNode(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.deleteNode(val)

        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.deleteNode(min_val)
        return self

def built_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    num = [88,7,12,14,15,20,27,23]
    numbers_tree = built_tree(num)

    print("In-Order:",numbers_tree.in_order_traversal())

    print("Pre-Order:",numbers_tree.pre_order_traversal())

    print("Post-Order:", numbers_tree.post_order_traversal())

    print("Min value:", numbers_tree.find_min())

    print("Max value:", numbers_tree.find_max())

    print("12 in num:",numbers_tree.search(12))

    numbers_tree.deleteNode(20)
    print("Delete Node 20:", numbers_tree.in_order_traversal())