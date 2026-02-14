# A doubly linked list is made up of Nodes.
# Each Node has 3 properties: its value, a pointer to the next node,
# and a pointer to the previous node.
class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    # When we initialize the list, it's empty.
    # So, both the head (first element) and tail (last element) are None.
    def __init__(self):
        self.head = None
        self.tail = None

    # This method adds one or more values to the end of the list.
    def append(self, *values):
        for item in values:
            new_node = Node(item)
            if self.head is None:
                # If the list is empty, the new node is both the head and the tail.
                self.head = new_node
                self.tail = new_node
            else:
                # If the list is not empty, add the new node after the current tail.
                self.tail.next_node = new_node
                new_node.prev_node = self.tail
                # Update the tail to be the new node.
                self.tail = new_node
        return self

    # This method prints the list from head to tail.
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next_node
        print("Forward: " + " -> ".join(elements))

    # This method shows the benefit of a doubly linked list: printing backward.
    def display_backward(self):
        if self.tail is None:
            print("List is empty")
            return

        elements = []
        current = self.tail
        while current:
            elements.append(str(current.value))
            current = current.prev_node
        print("Backward: " + " <- ".join(elements))

    # This method deletes the first node it finds with the given value.
    def delete(self, value):
        current = self.head

        # Traverse the list to find the node with the given value
        while current:
            if current.value == value:
                # --- Node to delete has been found ---

                # Case 1: It's NOT the head node (it has a previous node)
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                # Case 2: It IS the head node
                else:
                    self.head = current.next_node

                # Case 3: It's NOT the tail node (it has a next node)
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                # Case 4: It IS the tail node
                else:
                    self.tail = current.prev_node

                print(f"Deleted node with value: {value}")
                return  # Exit after deleting the first occurrence

            current = current.next_node

        print(f"Value {value} not found in the list.")


# --- Let's test the new DoublyLinkedList ---

dll = DoublyLinkedList()
print("Initial list:")
dll.display_forward()

print("\nAppending 3, 4, 5:")
dll.append(3, 4, 5)
dll.display_forward()
dll.display_backward()

print("\nDeleting 4 (a middle element):")
dll.delete(4)
dll.display_forward()
dll.display_backward()

print("\nDeleting 3 (the head element):")
dll.delete(3)
dll.display_forward()

print("\nDeleting 5 (the tail element):")
dll.delete(5)
dll.display_forward()

"""
This is another way of implementing but it users inheritance. 
If i inherit elements class in CustomLinkedList Class, it will mean that CustomLinkedList Class is a type of elements class
This is wrong. So, we should not implement it via inheritance.

class customLinkedList(elements):
    def __init__(self,element=None):
        super().__init__(element)
        self.element = element

    def printcustomlinkedlist(self):
        element = self.element
        print(f"Element: {element.value} NextElement: {element.nextelement}")

e1 = elements(100)
cl1 = customLinkedList(e1)

cl1.printcustomlinkedlist()
 """