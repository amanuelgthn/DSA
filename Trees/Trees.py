#!/usr/bin/python3
"""Trees implementation"""

class Node:
    """Representation of a single Node"""

    def __init__(self, element, parent=None):
        """initiallization of the Node"""
        self.element = element
        self.parent = parent
        self.children = []

    def add_child(self, element):
        """Add a child node to the current node."""
        child = Node(element, parent=self)
        self.children.append(child)
        return child
    
    def is_leaf(self):
        """check if the node is a leaf(has no children)"""
        return len(self.children)
    
    def is_root(self):
        """check if the node is the root (has no parent)"""
        return self.parent is None
    
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add_root(self, element):
        if self.root is not None:
            raise ValueError("Root already exists")
        self.root = Node(element)
        self.size = 1
        return self.root
    
    def add_child(self, parent, element):
        if parent is None:
            raise ValueError("Parent Node cannot be None")
        child = parent.add_child(element)
        self.size += 1
        return child
    
    def is_empty(self):
        return self.size == 0

    def __len__ (self):
        return self.size

    def num_children(self, node):
        return len(node.children)
    
    def traverse_preorder(self, node=None):
        if node is None:
            node = self.root
        result = [node.element]
        for child in node.children:
            result.extend(self.traverse_preorder(child))
        return result
    
    def traverse_postorder(self, node=None):
        if node is None:
            node = self.root
        result = []
        for child in node.children:
            result.extend(self.traverse_postorder(child))
        result.append(node.element)
        return result
    
    def height(self, node=None):
        if node is None:
            node = self.root
        if node.is_leaf():
            return 0
        return 1 + max(self.height(child) for child in node.children)
    
    def depth(self, node):
        depth = 0
        while node.parent is not None:
            node = node.parent
            depth +=1
        return depth
    