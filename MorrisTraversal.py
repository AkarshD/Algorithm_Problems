class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def MorrisTraversal(root):
    current = root

    while (current is not None):

        if current.left is None:
            print current.data,
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while (pre.right is not None and pre.right != current):
                pre = pre.right

                # Make current as right child of its inorder predecessor
            if (pre.right is None):
                pre.right = current
                current = current.left

                # Revert the changes made in if part to restore the
            # original tree i.e., fix the right child of predecssor
            else:
                pre.right = None
                print current.data,
                current = current.right


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')

MorrisTraversal(root)