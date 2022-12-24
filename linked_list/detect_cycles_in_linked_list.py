from linked_list import LinkedList


# two pointers approach
class CheckInfiniteLinkedList(LinkedList):
    def check_infinite(self):
        """Checks whether infinite loop via next"""
        pointer1 = pointer2 = self.head
        while pointer1 and pointer2:
            if pointer2.next is None:
                return False

            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

            if pointer1 is pointer2:
                return True
        return False
    

# my approach
def is_infinite_linked_list(head):
    visited_nodes = set()
    current_node = head

    while current_node:
        if id(current_node) not in visited_nodes:
            visited_nodes.add(id(current_node))
            current_node = current_node.next
        else:
            return True
    return False
