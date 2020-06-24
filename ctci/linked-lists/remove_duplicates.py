"""2.1 from Cracking the Coding Interview"""

class Node():
   """Node for singly linked lists."""

   def __init__(self, data, next=None):
    self.data = data
    self.next = next

   def __repr__(self):

    return f'<Node data={self.data} next={self.next.data if self.next else None}>'


def remove_duplicates(head_node:Node):
    """Remove duplicates from a linked list, given a head node."""

    seen = set()

    current = head_node
    previous = None

    while current:
        if current.data in seen:
            #remove node from linked list
            previous.next = current.next

        else:
            seen.add(current.data)
            previous = current

        current = current.next

def print_linked_list(head_node:Node):
    """Print a linked list's nodes"""

    current = head_node

    while current:
        print(current)
        current = current.next
    print("End of linked list")



#Testing
node_5 = Node(data="c")
node_4 = Node(data="a", next=node_5)
node_3 = Node(data="b", next=node_4)
node_2 = Node(data="b", next=node_3)
node_1 = Node(data="a", next=node_2)

def create_list_from_linked_list(head_node:Node):
    """Create an array of data from a linked_list"""
    results = []
    current = head_node
    while current:
        results.append(current.data)
        current = current.next

    return results


pre = create_list_from_linked_list(node_1)
remove_duplicates(node_1)
post = create_list_from_linked_list(node_1)

assert post != pre
assert sorted(post) == sorted(list(set(pre)))

