class Node:
    def __init__(self, value):
        """
        Initialize a new node with the given value.
        :param value: Value to be stored in the node.
        """
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        """
        Initializes the Binary Search Tree.
        """
        self.root = None

    def is_empty(self):
        """
        Check if the tree is empty.
        :return: True if the tree is empty, False otherwise.
        """
        return self.root is None

    def add(self, value):
        """
        Add a value to the BST.
        :param value: Value to be added to the BST.
        :return: True if the value is added, False otherwise.
        """
        if self.is_empty():
            self.root = Node(value)
            return True
        else:
            return self._add_recursive(self.root, value)

    def _add_recursive(self, current, value):
        """
        Helper method for recursively adding a value to the BST.
        :param current: The current node in the recursion.
        :param value: Value to be added.
        :return: True if the value is added, False otherwise.
        """
        if current.data > value:
            if current.left is None:
                current.left = Node(value)
                return True
            else:
                return self._add_recursive(current.left, value)
        elif current.data < value:
            if current.right is None:
                current.right = Node(value)
                return True
            else:
                return self._add_recursive(current.right, value)
        else:
            return False  # Value already in tree

    def print_tree(self, current, indent=""):
        """
        Print the BST in a readable format.
        :param current: The current node in the recursion.
        :param indent: Indentation for each level of the tree.
        """
        if current is not None:
            self.print_tree(current.right, indent + "   ")
            print(indent, current.data)
            self.print_tree(current.left, indent + "   ")

    def search(self, value):
        """
        Search for a value in the BST.
        :param value: Value to be searched.
        :return: True if the value is found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        """
        Helper method for recursively searching a value in the BST.
        :param current: The current node in the recursion.
        :param value: Value to be searched.
        :return: True if the value is found, False otherwise.
        """
        if current is None:
            return False
        if current.data == value:
            return True
        elif current.data > value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    def find_height(self, node):
        """
        Find the height of the binary search tree.
        :param node: The current node.
        :return: Height of the tree.
        """
        if node is None:
            return -1
        else:
            left_height = self.find_height(node.left)
            right_height = self.find_height(node.right)
            return 1 + max(left_height, right_height)

    def delete(self, value):
        """
        Delete a node with the specified value from the BST.
        :param value: Value of the node to be deleted.
        :return: The root node after deletion.
        """
        self.root, _ = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """
        Helper method for recursively deleting a node from the BST.
        :param node: The current node.
        :param value: Value of the node to be deleted.
        :return: Updated node after deletion.
        """
        if node is None:
            return node, False

        if value < node.data:
            node.left, deleted = self._delete_recursive(node.left, value)
        elif value > node.data:
            node.right, deleted = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.data = self._min_value_node(node.right).data
            node.right, _ = self._delete_recursive(node.right, node.data)

            return node, True

        if not deleted:
            return node, False

        return node, True

    def _min_value_node(self, node):
        """
        Find the node with the minimum value in the BST.
        :param node: The current node.
        :return: Node with the minimum value.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
