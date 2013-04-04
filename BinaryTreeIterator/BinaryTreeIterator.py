# define tree object
class Tree(object):
    def __init__(self, val):
        self.val = val;
        self.left = None
        self.right = None

class tree_iterator(object):
    def __init__(self, root_node):
        self.root_node = root_node
        self.node_stack = []
        root = root_node
        while root:
            self.node_stack.append(root)
            root = root.left

    def __iter__(self):
        return self

    def next(self):
        top = self.node_stack[-1]
        while not top and self.node_stack :
            self.node_stack.pop()
            top = self.node_stack[-1]
        if not top and not self.node_stack:
            raise StopIteration
        self.node_stack.pop()
        self.node_stack.append(top.right)
        return top.val

# using python generator
class tree_iterator2(object):
    def __init__(self, root_node):
        self.iter = treeiter(root_node)

    def __iter__(self):
        return self

    def next(self):
        return self.iter.next()

def treeiter(root_node):
    node_stack = []
    top = root_node
    while top or node_stack:
        if top:
            node_stack.append(top)
            top = top.left
        else:
            top = node_stack[-1]
            node_stack.pop()
            yield top.val
            top = top.right
