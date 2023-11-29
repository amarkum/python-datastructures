class Node:
    def __init__(self, data):
        """
        Initializes a new node with the given data.
        :param data: Data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initializes the LinkedList. Sets the head to None and size to 0.
        """
        self.size = 0
        self.head = None

    def is_empty(self):
        """
        Checks if the linked list is empty.
        :return: True if the list is empty, False otherwise.
        """
        return self.head is None

    def add_at_head(self, data):
        """
        Adds a new node with the specified data at the beginning of the linked list.
        :param data: Data to be added.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_at_end(self, data):
        """
        Adds a new node with the specified data at the end of the linked list.
        :param data: Data to be added.
        """
        if self.is_empty():
            self.add_at_head(data)
            return

        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    def print_all(self):
        """
        Prints all the elements of the linked list.
        """
        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete_at_head(self):
        """
        Deletes the first node of the linked list.
        """
        if self.is_empty():
            return
        self.head = self.head.next
        self.size -= 1

    def delete_by_value(self, value):
        """
        Deletes a node by its value.
        :param value: Value of the node to be deleted.
        """
        if self.is_empty():
            return

        if self.head.data == value:
            self.delete_at_head()
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def reverse(self):
        """
        Reverses the linked list in place.
        """
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def find_mid(self):
        """
        Finds the middle element of the linked list.
        :return: Data of the middle element.
        """
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None

    def print_mid_to_end(self):
        """
        Prints elements from the middle to the end of the linked list.
        """
        mid = self.find_mid()
        if mid:
            current = self.head
            while current:
                if current.data == mid:
                    break
                current = current.next

            while current:
                print(current.data)
                current = current.next

    def detect_loop(self):
        """
        Detects a loop in the linked list.
        :return: True if there's a loop, False otherwise.
        """
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
