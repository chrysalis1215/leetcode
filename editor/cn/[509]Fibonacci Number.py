# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache


class Solution:
    def fib(self, n: int) -> int:
        @cache
        def fib(self, n: int) -> int:
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return self.fib(n - 1) + self.fib(n - 2)
        
# leetcode submit region end(Prohibit modification and deletion)
