# 60ms O(nlongn)
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

# 56ms
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return

        def dfs(start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(start, mid - 1)
            node.right = dfs(mid + 1, end)
            return node

        return dfs(0, len(nums) - 1)

# 56ms
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, h):
            if l > h:
                return None
            m = l + (h - l) // 2
            node = TreeNode(nums[m])
            node.left = helper(l, m - 1)
            node.right = helper(m + 1, h)
            return node

        return helper(0, len(nums) - 1)


class Solution:
    value = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)

        self.value += root.val
        root.val = self.value

        if root.left:
            self.bstToGst(root.left)

        return root