# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            sorted_str = ''.join(sorted(word))
            hashmap[sorted_str].append(word)
        return list(hashmap.values())
        
# leetcode submit region end(Prohibit modification and deletion)
