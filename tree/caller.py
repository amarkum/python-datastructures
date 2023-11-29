from tree.binarysearchtreecustom import BinarySearchTree


class BinarySearchTreeCaller:
    @staticmethod
    def main():
        bst = BinarySearchTree()

        # Adding nodes to the BST
        bst.add(6)
        bst.add(4)
        bst.add(9)
        bst.add(5)
        bst.add(2)
        bst.add(8)
        bst.add(12)
        bst.add(10)
        bst.add(14)

        # Searching nodes
        print("Search for 108:", "Found" if bst.search(108) else "Not found")
        print("Search for 12:", "Found" if bst.search(12) else "Not found")

        # Printing the tree
        print("Binary Search Tree before deletion:")
        bst.print_tree(bst.root)

        # Deleting a node
        print("\nDeleting node 10")
        bst.delete(10)
        print("Binary Search Tree after deletion of 10:")
        bst.print_tree(bst.root)

        # Finding the height of the tree
        height = bst.find_height(bst.root)
        print("\nHeight of the tree:", height)

        # Additional tests can be added here for other methods, if any


if __name__ == "__main__":
    BinarySearchTreeCaller.main()
