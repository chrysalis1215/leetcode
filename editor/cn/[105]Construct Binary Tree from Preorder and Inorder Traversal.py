# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_dict = {
        pre_index = 0

        for i in range(len(inorder)):
            in_dict[inorder[i]] = i


        def buildSubTree(in_left, in_right) -> Optional[TreeNode]:
            nonlocal pre_index

            if in_left > in_right:
                return None

            root = TreeNode(preorder[pre_index])
            pre_index += 1

            root_index = in_dict[root.val]
            root.left = buildSubTree(in_left, root_index - 1)
            root.right = buildSubTree(root_index + 1, in_right)

            return root


        return buildSubTree(0, len(inorder) - 1)




        
# leetcode submit region end(Prohibit modification and deletion)
