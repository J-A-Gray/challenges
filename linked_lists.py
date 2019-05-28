class Node():
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node object. Data: {}; Next: {}>".format(
                                        self.data,
                                        self.next.data if self.next else None,
                                        )
class DLLNode():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return "<DLLNode object. Data: {}; Next: {}; Previous: {}>".format(
                                        self.data,
                                        self.next.data if self.next else None,
                                        self.prev.data if self.prev else None
                                        )

class DLinkedList():

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return "<Doubly Linked List. Head: {}; Tail: {}>".format(
                                        self.head.data if self.head else None,
                                        self.tail.data if self.head else None,
                                        )

    def append(self, data):
        """Append node with data to end of list"""
        new_node = DLLNode(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node




class LinkedList():
    """A linked list."""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return "<Linked List. Head: {}; Tail: {}>".format(
                                        self.head.data if self.head else None,
                                        self.tail.data if self.head else None,
                                        )

    def append(self, data):
        """Append node with data to end of lit"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


    def find(self, data):

        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False


    def print_list(self):

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def pop(self):
        if self.head is not None:
            current = self.head

            while current.next is not None:
                if current.next.next == None:
                    last = current.next
                    self.tail = current
                    current.next = None
                    return last
                else:
                    current = current.next

    def remove(self, data):

        #if removing head of LL, make 2nd item (if there is one) the new LL head
        if self.head is not None and self.head.data == data:
            self.head = self.head.next
            if self.head is None: #if there is no longer a head, LL is empty, set tail to None
                self.tail = None

        #Removing nodes other than the head node
        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return

            else:
                current = current.next

dll = DLinkedList()
print(dll)

dll.append("apple")
dll.append("berry")
dll.append("cherry")

print(dll)
print(dll.head.next)


# node1 = ll.pop()
# print(node1)
# print(ll)
# print(ll.tail)

