from collections import defaultdict
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = defaultdict(int)
        needs = defaultdict(int)
        res = []
        for i in p:
            needs[i] += 1

        left = right = 0

        for right, char in enumerate(s):
            if char in needs:
                window[char] += 1

            if window == needs:
                res.append(left)

            if right - left + 1 >= len(p):
                remove_char = s[left]
                if remove_char in window:
                    window[remove_char] -= 1
                    if window[remove_char] == 0:
                        del window[remove_char]
                left += 1

        return res
# leetcode submit region end(Prohibit modification and deletion)

Solution().findAnagrams('cbaebabacd', 'abc')