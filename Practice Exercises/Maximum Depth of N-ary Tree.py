class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def max_depth(root):
    if not root:
        return 0
    max_depth_child = 0
    for child in root.children:
        max_depth_child = max(max_depth_child, max_depth(child))
    return max_depth_child + 1

# Example usage
# Create a n-ary tree with a depth of 3: 1 -> [3, 2, 4], 3 -> [5, 6]
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
result = max_depth(root)
