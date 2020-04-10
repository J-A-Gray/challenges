class LinkedList:
    def __init__(self):
        head = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):

        return "<Node object. Data: {}; Next: {}>".format(
                                        self.val,
                                        self.next.val if self.next else None,
                                        )

def middleNode(head: ListNode) -> ListNode:
    """Find middle node in a singly-linked list, given the head node.

    >>> test1 = LinkedListFromArray([1, 2, 3])
    >>> middleNode(test1.head)
    <Node object. Data: 2; Next: 3>

    >>> test2 = LinkedListFromArray(list(range(1, 100001)))
    >>> middleNode(test2.head)
    <Node object. Data: 50001; Next: 50002>
    """

    #start two pointers at head node
    slow = fast = head

    while fast and fast.next:

        #slow pointer traverses LL one node at a time
        slow = slow.next
        #fast pointer traverses LL two nodes at a time
        fast = fast.next.next

    #when fast pointer reaches end of LL, slow pointer is at middle node    
    return slow


if __name__ == "__main__":
    
    class LinkedListFromArray:
        """For ease of testing"""
        def __init__(self, arg_list):
            self.head = None

            for arg in arg_list:
                var = ListNode(arg)
                if not self.head:
                    self.head = var
                    current = var
                else:
                    current.next = var
                    current = var

        def __repr__(self):

            return "<LinkedList object. Head: {}".format(
                                            self.head if self.head else None
                                            )
    
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")


