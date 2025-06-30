# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(path, total, start):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):

                path.append(candidates[i])
                total += candidates[i]
                backtrack(path, total, i)
                item = path.pop()
                total -= item

        backtrack([], 0, 0)

        return res
        
# leetcode submit region end(Prohibit modification and deletion)
