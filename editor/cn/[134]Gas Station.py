from typing import  List
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        cur = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                cur = i + 1
                tank = 0


        return (cur if cur < len(gas) else cur - len(gas) ) if total >=0  else -1
        
# leetcode submit region end(Prohibit modification and deletion)


Solution().canCompleteCircuit([2],	[2]
)