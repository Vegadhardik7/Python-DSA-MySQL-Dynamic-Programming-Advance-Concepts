class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.child = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + " ("  + self.designation +  ") "
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)

        if self.child:
            for child in self.child:
                child.print_tree(property_name)

    def add_child(self,child):
        child.parent = self
        self.child.append(child)

def build_management_tree():
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chimnay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    hr_head = TreeNode('Gels',"Hr Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    print("*" * 50)
    root_node.print_tree("designation")
    print("*" * 50)
    root_node.print_tree("both")