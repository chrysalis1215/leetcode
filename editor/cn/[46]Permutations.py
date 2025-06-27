# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i,  num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    path.append(num)
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return res


        
# leetcode submit region end(Prohibit modification and deletion)
