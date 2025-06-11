# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for i, bill in enumerate(bills):
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] > 0:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            else:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] > 2:
                    change[5] -= 3
                else:
                    return False

        return True

        
# leetcode submit region end(Prohibit modification and deletion)
