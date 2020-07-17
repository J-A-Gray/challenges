class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):

        return f'<Node value {self.val}>'

def merge_two_sorted_linked_lists(l1, l2) -> Node:
    """Merge two sorted linked lists and return head node of new sorted linked
    list.

    >>> l1_root = Node(val=1, next=Node(val=2, next=Node(val=4)))
    >>> l2_root = Node(val=1, next=Node(val=5, next=Node(val=6)))
    >>> current = merge_two_sorted_linked_lists(l1_root, l2_root)
    >>> current.val == 1
    True

    >>> current.next.next.next.next.val == 5
    True

    """

    #create a Node to be previous to node to return
    placeholder = Node(-1)

    previous = placeholder

    while l1 and l2:
        if l1.val <= l2.val:
            previous.next = l1
            l1 = l1.next

        else:
            previous.next = l2
            l2 = l2.next

        previous = previous.next

    previous.next = l1 if l1 is not None else l2

    return placeholder.next
