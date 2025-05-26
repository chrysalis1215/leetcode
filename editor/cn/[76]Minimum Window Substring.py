# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter
        needs = Counter(t)
        res = ''
        windowQueue = deque()

        left = right = 0
        while right < len(s):
            char = s[right]
            if char in needs:
                window[char] += 1
                windowQueue.append(right)

            right += 1

            # shrink the window to the mini set
            while Counter(window) >= needs:
                # left 跳至 s 的有效字符位置
                left = windowQueue.popleft()
                if res == '' or right - left < len(res):
                    res = s[left: right]

                # 收缩窗口，更新 left 位置
                remove_char = s[left]
                window[remove_char] -= 1

                # left 跳至 s 下一个有效字符位置
                if windowQueue:
                    left = windowQueue[0]

        return res
# leetcode submit region end(Prohibit modification and deletion)

Solution().minWindow('abc', 'bc')