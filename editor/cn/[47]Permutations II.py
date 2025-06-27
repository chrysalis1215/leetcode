# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue

                if not used[i]:
                    used[i] = True
                    path.append(num)
                    backtrack(path, used)
                    path.pop()
                    used[i] = False



        backtrack([], [False] * len(nums))
        return res


# leetcode submit region end(Prohibit modification and deletion)
