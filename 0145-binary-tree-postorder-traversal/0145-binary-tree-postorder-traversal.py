class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, res):
            if(not node): return res
            if(not node.left and not node.right):
                res.append(node.val)
                return res
            res = dfs(node.left, res)
            res = dfs(node.right, res)
            res.append(node.val)
            return res
        return dfs(root, [])