class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def getTreeValues(self):
        ans, items, queue = [], [], []
        if not self:
            return self
        queue.append(self)
        while queue:
            curr = queue.pop(0)
            items.append(curr)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        for item in items:
            ans.append(item.val)
        return ans
