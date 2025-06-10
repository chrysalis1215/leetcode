# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter, defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        locations = {}
        dict = defaultdict(int)
        for index, value in enumerate(s):
            locations[value] = index
            dict[value] += 1

        for key, value in dict.items():
            if value == 1:
                return locations[key]

        return -1

        
# leetcode submit region end(Prohibit modification and deletion)
