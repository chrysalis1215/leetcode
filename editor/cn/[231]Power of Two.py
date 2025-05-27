# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n  > 0 and n&(n-1) == 0
        
# leetcode submit region end(Prohibit modification and deletion)
