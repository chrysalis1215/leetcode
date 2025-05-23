from collections import defaultdict

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        needs = {}
        for i in s1:
            needs[i] = needs.get(i, 0) + 1

        left = right = 0
        len_s1 = len(s1)

        while right < len(s2):
            char = s2[right]
            window[char] += 1
            right += 1

            # shrink the window
            if right - left > len_s1:
                char_remove = s2[left]
                left += 1
                window[char_remove] -= 1
                if window[char_remove] == 0:
                    del window[char_remove]

            if window == needs:
                return True

        return False


# leetcode submit region end(Prohibit modification and deletion)
Solution().checkInclusion('adc', 'dcda')