'''

Internally to implement set one of the ways you can use is
Binary Search Tree.


Binary Tree: Is a regular tree with constraint is that it has
at max 2 child nodes.

Binary Search Tree: Left < Mid < Right & Elements are not duplicated

                        15
                        |
                 |-------------|
                12             27
                |              |
         |-----------|   |-----------|
         7          14  20           88
                        |
                        -----|
                             23


* If you want to search through binary search tree there is:
-> BFS (Breadth First Search)
-> DFS (Depth First Search)
    - in order traversal      [7,12,14,15,20,23,27,88]
    - pre order traversal     [15,12,7,14,27,20,23,88]
    - post order traversal    [7,14,12,23,20,88,27,15]
'''

class BinarySeachTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left sub-tree
            if self.left: # Check if left element has some value
                self.left.add_child(data)
            else:         # Left node is empty
                self.left = BinarySeachTreeNode(data)

        if data > self.data:
        # add data in right sub-tree
            if self.right: # Check if right element has some value
                self.right.add_child(data)
            else:         # Left node is empty
                self.right = BinarySeachTreeNode(data)


    def in_order_traversal(self):
        '''
            This method will return list of element in our binary tree in specific order.
        '''

        elements = []

        # Visit left node
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base node
        elements.append(self.data)

        # Visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val) # Recursion for search
            else:
                return False


        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)  # Recursion for search
            else:
                return False


def built_tree(elements):
    root = BinarySeachTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    num = [17,4,1,20,9,23,18,34,18,9,9,9]
    numbers_tree = built_tree(num)

    print(numbers_tree.in_order_traversal())

    print(numbers_tree.search(1))


    # ----------------------------------

    county = ["Russia", "India", "USA", "UK", "UAE", "Israel", "France"]
    county_tree = built_tree(county)

    print("Countries: ",county_tree.in_order_traversal())

    print("Is Spain in country: ",county_tree.search("Spain"))






















