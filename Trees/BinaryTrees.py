#!/usr/bin/python3
class BinaryTreeNode:
    """Representation of a single Binary Tree Node"""
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left  # Points to the left child
        self.right = right  # Points to the right sibling


class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse_preorder(self, node=None):
        if node is None:
            node = self.root
        result = [node.element]
        if node.left:
            result += self.traverse_preorder(node.left)  # Concatenate lists
        if node.right:
            result += self.traverse_preorder(node.right)
        return result

    def traverse_inorder(self, node=None):
        #visit/print left nnode of thhe tree before the right branch
        if node is None:
            node = self.root
        result = []
        if node.left:
            result += self.traverse_inorder(node.left)  # Concatenate lists
        result.append(node.element)
        if node.right:
            result += self.traverse_inorder(node.right)
        return result

    def traverse_postorder(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node.left:
            result += self.traverse_postorder(node.left)  # Concatenate lists
        if node.right:
            result += self.traverse_postorder(node.right)
        result.append(node.element)
        return result


    def convert_to_binary_tree(general_tree_node):
        """Convert a general tree node to a binary tree node using LCRS."""
        if general_tree_node is None:
            return None

        # Create a binary tree node for the current general tree node
        binary_node = BinaryTreeNode(general_tree_node.element)

        # Convert the first child to the left child in the binary tree
        if general_tree_node.children:
            binary_node.left = convert_to_binary_tree(general_tree_node.children[0])

        # Convert siblings to the right child in the binary tree
        current = binary_node.left
        for sibling in general_tree_node.children[1:]:
            current.right = convert_to_binary_tree(sibling)
            current = current.right

        return binary_node


# Example usage:
if __name__ == "__main__":
    # Create a general tree
    tree = Tree()
    root = tree.add_root("A")
    b = tree.add_child(root, "B")
    c = tree.add_child(root, "C")
    d = tree.add_child(root, "D")
    e = tree.add_child(b, "E")
    f = tree.add_child(b, "F")
    g = tree.add_child(d, "G")

    # Convert the general tree to a binary tree
    binary_tree = BinaryTree()
    binary_tree.root = convert_to_binary_tree(tree.root)

    # Traverse the binary tree
    print("Preorder traversal of binary tree:", binary_tree.traverse_preorder())
    print("Inorder traversal of binary tree:", binary_tree.traverse_inorder())
    print("Postorder traversal of binary tree:", binary_tree.traverse_postorder())
