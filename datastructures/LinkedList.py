"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular data.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        pass

    def printList(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

    def delete(self, data):
        """Delete the first node with a given data."""

        prev = None
        current = self.head

        while current.data != data and current.next:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

        if current.data == data:
            prev.next = current.next
        else:
            self.head

            # Test cases
            # Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
Ll = LinkedList(e1)
Ll.append(e2)
Ll.append(e3)
Ll.append(e4)

# Test get_position
# Should print 3
# print(Ll.head.next.next.data)
# # Should also print 3
# print(Ll.get_position(3).data)

# # Test insert
# Ll.insert(e4, 3)
# # Should print 4 now
# print(Ll.get_position(3).data)

# Test delete
Ll.printList()
Ll.delete(1)
Ll.printList()

# # Should print 2 now
# print(Ll.get_position(1).data)
# # Should print 4 now
# print(Ll.get_position(2).data)
# # Should print 3 now
# print(Ll.get_position(3).data)
