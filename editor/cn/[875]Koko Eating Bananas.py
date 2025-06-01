# leetcode submit region begin(Prohibit modification and deletion)
import math
from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_k = 1
        max_k = max(piles)


        while min_k < max_k:
            mid_k = (min_k + max_k) // 2

            last_h = sum(ceil(p / mid_k) for p in piles)

            if last_h > h:
                min_k = mid_k + 1
            else:
                max_k = mid_k

        return min_k

        
# leetcode submit region end(Prohibit modification and deletion)
