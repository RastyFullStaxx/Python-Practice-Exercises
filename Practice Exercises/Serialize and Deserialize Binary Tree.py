class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def dfs(node):
        if node:
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        else:
            values.append("null")

    values = []
    dfs(root)
    return ','.join(values)

def deserialize(data):
    def dfs():
        val = next(values)
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node

    values = iter(data.split(','))
    return dfs()

# Example usage
# Create a binary tree: 1 -> 2 -> 3 -> null -> null -> 4 -> 5
root = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(4, None, TreeNode(5)))
serialized_tree = serialize(root)
deserialized_root = deserialize(serialized_tree)
