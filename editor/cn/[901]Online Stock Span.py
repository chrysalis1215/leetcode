# leetcode submit region begin(Prohibit modification and deletion)
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.list = []

    def next(self, price: int) -> int:
        self.list.append(price)
        size = len(self.list)
        while self.stack and price >= self.list[self.stack[-1]]:
            self.stack.pop()
        cur_index = size - 1
        short_after_max = 0 if not self.stack else self.stack[-1] + 1

        res = cur_index - short_after_max
        self.stack.append(cur_index)
        return res + 1




        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# leetcode submit region end(Prohibit modification and deletion)
