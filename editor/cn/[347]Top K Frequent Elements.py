from collections import Counter, defaultdict

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Sort by frequency descending
        return [num for num, freq in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]
# leetcode submit region end(Prohibit modification and deletion)
