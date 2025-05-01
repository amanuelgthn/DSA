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

    def height(self, node=None):
        if node is None:
            node = self.root
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1 
    
    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            self.display(node.right, level + 1)
            print("    " * level + str(node.element))
            self.display(node.left, level + 1)

        

    def convert_to_binary_tree(self, general_tree_node):
        if general_tree_node is None:
            return None

        binary_node = BinaryTreeNode(general_tree_node.element)

        if general_tree_node.children:
            binary_node.left = self.convert_to_binary_tree(general_tree_node.children[0])

        current = binary_node.left
        for sibling in general_tree_node.children[1:]:
            current.right = self.convert_to_binary_tree(sibling)
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
    print("Height of binary tree:", binary_tree.height())
    print("Display of binary tree:")
    binary_tree.display()
