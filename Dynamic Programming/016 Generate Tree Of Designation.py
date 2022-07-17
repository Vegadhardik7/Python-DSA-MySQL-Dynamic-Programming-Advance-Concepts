class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):   # get level of node
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_Tree(self):
        spaces = ' ' * self.get_level() * 3

        prefix = spaces + "|--> " if self.parent else ""

        print(prefix + self.data)
        if len(self.data)>0:
            for child in self.child:
                child.print_Tree()

def name():
    ceo_root = TreeNode("Nilupul")

    cto_child = TreeNode("Chinmay")

    if_head_child = TreeNode("Vishwa")
    if_head_child.add_child(TreeNode("Dhaval"))
    if_head_child.add_child(TreeNode("Abhijit"))

    hr_head = TreeNode("Gels")

    hr_head.add_child(TreeNode("Peter"))
    hr_head.add_child(TreeNode("Waqas"))

    app_head = TreeNode("Aamir")

    cto_child.add_child(if_head_child)
    cto_child.add_child(app_head)


    ceo_root.add_child(cto_child)
    ceo_root.add_child(hr_head)

    return ceo_root


def designation():
    ceo = TreeNode("CEO")

    cto = TreeNode("CTO")

    if_head_child = TreeNode("Infrastructure Head")
    if_head_child.add_child(TreeNode("Cloud Manager"))
    if_head_child.add_child(TreeNode("App Manager"))

    hr_head = TreeNode("Hr Head")

    hr_head.add_child(TreeNode("Recruitment Manager"))
    hr_head.add_child(TreeNode("Policy Manager"))

    app_head = TreeNode("Application Head")

    cto.add_child(if_head_child)
    cto.add_child(app_head)


    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == "__main__":
    root1 = name()
    root2 = designation()
    root1.print_Tree()
    root2.print_Tree()
    pass