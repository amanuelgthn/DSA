#!/usr/bin/python3
from Trees import Tree


if __name__ == "__main__":
    # Create a general tree
    tree = Tree()
    
    # Add root and children
    root = tree.add_root("Root")
    child1 = tree.add_child(root, "Child 1")
    child2 = tree.add_child(root, "Child 2")
    grandchild1 = tree.add_child(child1, "Grandchild 1")
    grandchild2 = tree.add_child(child1, "Grandchild 2")
    grandchild3 = tree.add_child(child2, "Grandchild 3")

    # Tree properties
    print(f"Tree size: {len(tree)}")
    print(f"Tree is empty? {tree.is_empty()}")
    print(f"Root's children: {[child.element for child in root.children]}")
    print(f"Height of the tree: {tree.height()}")
    print(f"Depth of 'Grandchild 1': {tree.depth(grandchild1)}")
    
    # Traversing the tree
    print("Preorder Traversal:")
    for elem in tree.traverse_preorder():
        print(elem)

    print("Postorder Traversal:")
    for elem in tree.traverse_postorder():
        print(elem)
