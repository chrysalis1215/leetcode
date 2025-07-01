# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(path, total, used, start):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return


            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1] and not used[i - 1]:
                    continue

                if not used[i]:
                    used[i] = True
                    path.append(candidates[i])
                    backtrack(path, total + candidates[i], used, i + 1)
                    path.pop()
                    used[i] = False



        backtrack([], 0, [False] * len(candidates), 0)

        return res

        
# leetcode submit region end(Prohibit modification and deletion)
