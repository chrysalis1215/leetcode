# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] += 1

        sorted_desc = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))

        return ''.join(k * v for k, v in sorted_desc.items())



        
# leetcode submit region end(Prohibit modification and deletion)
