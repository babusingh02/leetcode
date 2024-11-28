"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return
        root.next=None
        if not root.left:
            if not root.right:return root
            q=[root.right,None]
        else:
            if root.right:q=[root.left,root.right,None]
            else:q=[root.left,None]
        while q:
            node=q.pop(0)
            if node is None:
                if not q:return root
                q.append(None)
                continue
            node.next=q[0]
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
        