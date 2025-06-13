# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from itertools import count
from typing import List

class FreqStack:

    def __init__(self):
        self.group = defaultdict(list)
        self.count = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.count[val] + 1
        self.group[freq].append(val)
        self.count[val] = freq

        self.max_freq = max(self.max_freq, freq)


    def pop(self) -> int:

        max_freq_group =  self.group[self.max_freq]
        val = max_freq_group.pop()
        self.count[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# leetcode submit region end(Prohibit modification and deletion)
