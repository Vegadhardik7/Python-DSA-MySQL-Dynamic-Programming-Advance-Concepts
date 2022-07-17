class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, kids):          # when we will append to child node it will become parent
        kids.parent = self
        self.child.append(kids)


    def get_level(self):   # get level of node
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_Tree(self):
        spaces = ' ' * self.get_level() * 3

        prefix = spaces + "|-->" if self.parent else ""

        print(prefix + self.data)
        if len(self.child)>0:
            for child in self.child:
                child.print_Tree()

def build_product_trees():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")

    laptop.add_child(TreeNode("Mac-pro"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Google-Book"))



    cellphone = TreeNode("Cellphone")

    cellphone.add_child(TreeNode("Galaxy-z"))
    cellphone.add_child(TreeNode("Nokia-3663"))
    cellphone.add_child(TreeNode("iPhone-12"))



    tv = TreeNode("Tv")

    tv.add_child(TreeNode("Onida"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Samsung"))


    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_trees()
    # print(root.get_level())
    root.print_Tree()
    pass
