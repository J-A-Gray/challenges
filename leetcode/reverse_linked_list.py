class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_items_values(self):
        current = self.head

        while current:
            print(current.val)
            current = current.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'<ListNode value={self.val}>'

#iterative
def reverse_linked_list(head_node):
    """
    >>> node_4 = ListNode(val=4)
    >>> node_2 = ListNode(val=2, next=node_4)
    >>> node_1 = ListNode(val=1, next=node_2) 
    >>> reverse_linked_list(node_1)
    <ListNode value=4>

    >>> ll1 = LinkedList(head=node_4)
    >>> ll1.print_items_values()
    4
    2
    1

    """
    #create a current node, set head to current
    current = head_node
    #create a temp variable
    temp = None

    while current is not None:
        #store current node's next so we can overwrite current.next
        next_node = current.next
        #reset to node held in temp
        current.next = temp
        #move current node into temp
        temp = current
        #move through the linked list
        current = next_node

    head_node = temp

    return head_node

