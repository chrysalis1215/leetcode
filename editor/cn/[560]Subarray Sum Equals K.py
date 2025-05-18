from typing import List

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums)
        s = [0] * (size + 1)
        restDic = {}
        ans = 0
        for i, num in enumerate(nums):
            s[i + 1] = s[i] + num
            # 先判断当前位置是否可以和已有位置组成 目标子序列
            if s[i + 1] in restDic:
                ans += restDic[s[i + 1]]

            if s[i+1] == k:
                ans += 1
            restKey1 = s[i + 1] + k

            restDic[restKey1] = restDic.get(restKey1, 0) + 1


        return ans


        
# leetcode submit region end(Prohibit modification and deletion)
Solution().subarraySum(
    [0,0,0,0,0,0,0,0,0,0],
0
)