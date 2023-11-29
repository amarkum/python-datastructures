from linkedlist.linkedlistcustom import LinkedList


class Caller:
    @staticmethod
    def create_intersection(node_one, node_two):
        """
        Creates an intersection between two linked lists.
        The third node of the first linked list points to the second node of the second linked list.
        """
        node_one.next.next.next = node_two.next.next

    @staticmethod
    def find_intersection(head_one, head_two):
        """
        Finds the intersection point of two linked lists, if it exists.
        """
        pointer_a = head_one
        pointer_b = head_two

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else head_two
            pointer_b = pointer_b.next if pointer_b else head_one

        return pointer_a


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_at_end("2")
    linked_list.add_at_end("4")
    linked_list.add_at_end("6")
    linked_list.add_at_end("7")

    # Delete a value from the linked list
    linked_list.delete_by_value("4")

    # Print all elements of the linked list
    print("All Elements of LinkedList")
    linked_list.print_all()

    # Print elements from the middle to the end of the linked list
    print("Middle to Last of LinkedList")
    linked_list.print_mid_to_end()

    # Reverse the linked list
    linked_list.reverse()
    print("LinkedList Reversed")

    # Print the size of the linked list
    print("Size of the List:", linked_list.size)

    # Add more elements to the end of the linked list
    linked_list.add_at_end("15")
    linked_list.add_at_end("9")
    linked_list.add_at_end("23")
    linked_list.add_at_end("2")

    # Detect a loop in the linked list
    print("Does LinkedList have a Loop:", linked_list.detect_loop())

    linked_list_two = LinkedList()
    linked_list_two.add_at_end("2")
    linked_list_two.add_at_end("4")
    linked_list_two.add_at_end("6")
    linked_list_two.add_at_end("7")
    linked_list_two.add_at_end("33")

    linked_list_three = LinkedList()
    linked_list_three.add_at_end("91")
    linked_list_three.add_at_end("88")
    linked_list_three.add_at_end("53")

    # Create an intersection between two linked lists
    Caller.create_intersection(linked_list_two.head, linked_list_three.head)
    linked_list_three.print_all()

    # Find the intersection point between two linked lists
    intersection_node = Caller.find_intersection(linked_list_two.head, linked_list_three.head)
    if intersection_node:
        print("Intersection Node Data:", intersection_node.data)
