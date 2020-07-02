from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

 # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
def traverse_bt(root) -> list:
    q = deque()

    results = []
    current = root

    while current:
        print("Current node is", current.val)
        results.append(current.val)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
        if q:
            current = q.popleft()
        else:
            return results

def traverse_bt_bottom_up(root) -> list:
    to_visit = deque() #a queue, append to right and popleft from left
    results = deque() #a stack
    current = root

    while current:
        print("Current node is", current.val)
        results.append(current.val)

        #going right first because we'll do it in reverse order
        to_visit.append(current.right) if current.right else print("Nope") 
        to_visit.append(current.left) if current.left else print("Nope") 
        

        if to_visit:
            current = to_visit.popleft()
        else:
            return list(reversed(results))



n15, n7 = TreeNode(val=15), TreeNode(val=7)
n9, n20 = TreeNode(val=9), TreeNode(val=20, left=n15, right=n7)
n3 = TreeNode(val=3, left=n9, right=n20)

# assert traverse_bt(n3) == [[3], [9, 20], [15, 7]]
# assert traverse_bt(n20) == [[20], [15, 7]]

